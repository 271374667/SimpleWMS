import loguru

from src.dict_typing import RetrievalDict
from src.model.retrieval_model import RetrievalModel
from src.table_handler import TableHandler
from src.view.retrieval_view import RetrievalView


class RetrievalPresenter:
    def __init__(self):
        self._count = 0
        self._view = RetrievalView()
        self._model = RetrievalModel()
        self._table_handler = TableHandler(self.get_view().get_table_widget(), RetrievalDict)
        self.get_view().get_display_lcd().display(self.get_model().get_wave_lastest_number())
        self._connect_signals()

    def get_view(self) -> RetrievalView:
        return self._view

    def get_model(self) -> RetrievalModel:
        return self._model

    def _clear_all_table(self) -> None:
        ui = self.get_view()
        result = ui.show_mask_dialog(title='清空表格', content='确定要清空表格吗？')
        if result:
            self._table_handler.clear()

    def _delete_current_row(self) -> None:
        ui = self.get_view()
        current_row = ui.get_table_widget().currentRow()
        if current_row == -1:
            ui.show_warning_infobar(title='没有选中任何行！', content='请选中要删除的行')
            return
        result = ui.show_mask_dialog(title='删除当前行', content='确定要删除当前行吗？')
        if result:
            ui.get_table_widget().removeRow(current_row)

    def _new_retrieval(self) -> None:
        self._count += 1
        ui = self.get_view()
        input_lineedit = ui.get_input_lineedit()
        input_text = input_lineedit.text()
        input_lineedit.clear()
        ui.get_output_textedit().appendPlainText(f'No.{self._count}内容:{input_text}')

        # 如果输入为空，那么就不做任何处理
        if not input_text:
            return

        # 如果输入的是数字，那么就根据EAN13查询
        if not input_text.isdigit():
            self.get_view().show_warning_infobar(title='必须是数字!', content='请输入正确的EAN13,输入必须为数字')
            return

        # 检测是否是真实的EAN13
        if not self.get_model().is_real_ean13(input_text):
            ui.show_warning_infobar(title='不是正确的EAN13',
                                    content=f'请输入正确的EAN13，检查您的输入:{input_text}')
            return

        # 检测表格中是否已经存在该商品
        for row in range(ui.get_table_widget().rowCount()):
            if self.get_view().is_row_empty(row):
                break
            elif input_text == ui.get_table_widget().item(row, 5).text():
                ui.show_warning_infobar(title='商品已经存在',
                                        content=f'EAN13为{input_text}的商品在表格中已经存在,不要重复添加')
                return

        inventory = self.get_model().get_inventory_by_ean13(input_text)
        if inventory is None:
            ui.show_warning_infobar(title='没有找到该商品', content=f'没有找到EAN13为{input_text}的商品')
            return

        # 检测商品是否已经出库
        if (self.get_model().is_inventory_sold(input_text)
                and not ui.get_is_repeat_switch_button().isChecked()):
            ui.show_warning_infobar(title='商品已经出库', content=f'EAN13为{input_text}的商品已经出库')
            return

        wave_serial_number = self.get_model().get_wave_lastest_serial_number()

        new_data: RetrievalDict = {
                "name": inventory.name,
                "brand": inventory.brand,
                "price": str(inventory.price),
                "wave_serial_number": wave_serial_number,
                "storage_time": str(inventory.storage_time),
                "ean13": inventory.ean13,
                }
        self._table_handler.add_row(new_data)
        loguru.logger.debug(f'添加了一行数据:{inventory}')

    def _export_data(self) -> None:
        # TODO: 未来将会做成多线程
        mask_title = '确认出库?'
        mask_content = '点击确认将会清空表格并将数据写入到数据库然后输出xlsx,出库之后无法重新入库,重新入库会当成两件衣服处理,请谨慎操作'
        if not self.get_view().show_mask_dialog(title=mask_title, content=mask_content):
            return

        ui = self.get_view()
        # data = ui.get_data()
        data = self._table_handler.get_data()
        if not data:
            ui.show_warning_infobar(title='无数据', content='当前没有任何数据可以导出,导出操作已终止')
            return
        self.get_model().export_data(data)

        ui.show_success_infobar(title='导出成功', content='文件被成功导出,您可以在指定文件夹下查看对应文件',
                                duration=-1)
        ui.get_display_lcd().display(self.get_model().get_wave_lastest_number())
        ui.get_table_widget().clearContents()

    def _on_batch_spinbox_value_changed(self, value: int) -> None:
        ui = self.get_view()
        latest_wave_number = self.get_model().get_wave_lastest_number()
        if value > latest_wave_number + 1:
            ui.show_warning_infobar(title='波次号错误', content='波次号不能大于最新的波次号 + 1')
            ui.get_wave_spinbox().setValue(latest_wave_number + 1)
            return

    def _connect_signals(self) -> None:
        ui = self.get_view()
        ui.get_confirm_input_button().clicked.connect(self._new_retrieval)
        ui.get_input_lineedit().returnPressed.connect(self._new_retrieval)
        ui.get_clear_table_button().clicked.connect(self._clear_all_table)
        ui.get_delete_current_row_button().clicked.connect(self._delete_current_row)
        ui.get_output_table_button().clicked.connect(self._export_data)
        ui.get_wave_spinbox().valueChanged.connect(self._on_batch_spinbox_value_changed)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    storage_presenter = RetrievalPresenter()
    storage_presenter.get_view().show()
    app.exec()
