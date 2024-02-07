import loguru

from src.dict_typing import StorageDict
from src.model.storage_model import StorageModel
from src.table_handler import TableHandler
from src.utils.run_in_thread import RunInThread
from src.view.storage_view import StorageView


class StoragePresenter:
    def __init__(self):
        self._view = StorageView()
        self._model = StorageModel()
        self._table_handler = TableHandler(self.get_view().get_table_widget(),
                                           StorageDict)
        self.get_view().get_display_lcd().display(self.get_model().get_newest_batch_number())
        self._connect_signals()

    def get_view(self) -> StorageView:
        return self._view

    def get_model(self) -> StorageModel:
        return self._model

    def _on_confirm_button_clicked(self) -> None:
        ui = self.get_view()
        item_name = ui.get_clothes_name_lineedit().text()
        brand = ui.get_brand_lineedit().text()
        price = ui.get_price_doublespinbox().value()
        batch = ui.get_batch_spinbox().value()
        quantity = ui.get_print_number_spinbox().value()
        auto_switch = ui.get_auto_switch_button().isChecked()

        if not item_name:
            ui.get_clothes_name_lineedit().setFocus()
            ui.show_warning_infobar(title='衣服名称为空！', content='请重新输入衣服名称')
            loguru.logger.debug('衣服名称为空！')
            return

        if not brand:
            ui.get_brand_lineedit().setFocus()
            ui.show_warning_infobar(title='品牌为空！', content='请重新输入品牌')
            loguru.logger.debug('品牌为空！')
            return

        if not price or price == 0:
            ui.get_price_doublespinbox().setFocus()
            ui.show_warning_infobar(title='价格不能为零或者空！', content='请重新输入价格')
            loguru.logger.debug('价格不能为零或者空！')
            return

        if not auto_switch:
            latest_batch = self.get_model().get_newest_batch_number()
            if batch > latest_batch + 1:
                ui.show_warning_infobar('批次过大!', '您的批次号不能超过当前最新的批次号+1')
                loguru.logger.debug('批次过大!')
                return

            # 将数据添加到表格中
            new_data_list: list[StorageDict] = []
            for _ in range(quantity):
                new_data: StorageDict = {
                        'name': item_name,
                        'brand': brand,
                        'price': str(price),
                        'batch_serial_number': self.get_model().gen_batch_serial_number(batch)
                        }
                new_data_list.append(new_data)
            self._table_handler.add_rows(new_data_list)
            return

        # 如果是自动切换，那么就需要先获取最新的批次
        batch_serial_number = self.get_model().get_newest_batch_serial_number()
        new_data_list: list[StorageDict] = []
        for _ in range(quantity):
            new_data: StorageDict = {
                    "name": item_name,
                    "brand": brand,
                    "price": str(price),
                    "batch_serial_number": batch_serial_number
                    }
            new_data_list.append(new_data)
        self._table_handler.add_rows(new_data_list)
        loguru.logger.debug(f'添加了一行数据:{item_name} {brand} {price} {batch_serial_number} {quantity}')

    def _clear_all_table(self) -> None:
        ui = self.get_view()
        result = ui.show_mask_dialog(title='清空表格', content='确定要清空表格吗？')
        if result:
            self._table_handler.clear()
            loguru.logger.debug('清空了表格')

    def _delete_current_row(self) -> None:
        ui = self.get_view()
        current_row = ui.get_table_widget().currentRow()
        if current_row == -1:
            ui.show_warning_infobar(title='没有选中任何行！', content='请选中要删除的行')
            return
        result = ui.show_mask_dialog(title='删除当前行', content='确定要删除当前行吗？')
        if result:
            ui.get_table_widget().removeRow(current_row)
            loguru.logger.debug(f'删除了一行数据:{current_row}')

    def _export_data_to_excel(self) -> None:
        """导出数据到Excel"""
        mask_title = '确认添加?'
        mask_content = '点击确认将会清空表格并将数据添加到数据库,在还没添加之前您可以在表格里面对数据双击进行修改'
        if not self.get_view().show_mask_dialog(title=mask_title, content=mask_content):
            return

        data = self._table_handler.get_data()
        if not data:
            self.get_view().show_warning_infobar(title='没有数据！', content='请先添加数据')
            return

        def run_func():
            self.get_model().export_data(data)

        def finish_func():
            self.get_view().finish_state_tooltip()
            self.get_view().show_success_infobar(title='导出成功！', content='数据已经成功导出到Excel和数据库中!',
                                                 duration=-1)
            self.get_view().get_table_widget().clearContents()
            loguru.logger.info('导出了数据到Excel和数据库')

        self._run_in_thread = RunInThread()
        self._run_in_thread.set_start_func(run_func)
        self._run_in_thread.set_finished_func(finish_func)
        self._run_in_thread.start()
        state_pos = self.get_view().get_save_table_button().frameGeometry().topLeft()
        print(state_pos)
        self.get_view().show_state_tooltip('正在导出数据',
                                           '请稍等...',
                                           state_pos.x() - 20,
                                           state_pos.y() - 40)

    def _connect_signals(self) -> None:
        ui = self.get_view()
        ui.get_confirm_button().clicked.connect(self._on_confirm_button_clicked)
        ui.get_clear_table_button().clicked.connect(self._clear_all_table)
        ui.get_delete_current_row_button().clicked.connect(self._delete_current_row)
        ui.get_delete_current_row_button().clicked.connect(
                lambda: self.get_view().finish_state_tooltip('成功!', '清除完成'))
        ui.get_save_table_button().clicked.connect(self._export_data_to_excel)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    storage_presenter = StoragePresenter()
    storage_presenter.get_view().show()
    app.exec()
