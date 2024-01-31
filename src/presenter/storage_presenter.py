from typing import List, Tuple

import loguru

from src.model.storage_model import StorageModel
from src.view.storage_view import StorageView


class StoragePresenter:
    def __init__(self):
        self._table_headers = ['名称', '品牌', '价格', '批次']
        self._view = StorageView()
        self._model = StorageModel()
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
            return

        if not brand:
            ui.get_brand_lineedit().setFocus()
            ui.show_warning_infobar(title='品牌为空！', content='请重新输入品牌')
            return

        if not price or price == 0:
            ui.get_price_doublespinbox().setFocus()
            ui.show_warning_infobar(title='价格不能为零或者空！', content='请重新输入价格')
            return

        if not auto_switch:
            latest_batch = self.get_model().get_newest_batch_number()
            if batch > latest_batch + 1:
                ui.show_warning_infobar('批次过大!', '您的批次号不能超过当前最新的批次号+1')
                return

            self.get_view().add_table_row(item_name, brand,
                                          str(price),
                                          self.get_model().gen_batch_serial_number(batch),
                                          str(quantity))
            return

        # 如果是自动切换，那么就需要先获取最新的批次
        batch_serial_number = self.get_model().get_newest_batch_serial_number()
        self.get_view().add_table_row(item_name, brand, str(price), batch_serial_number, str(quantity))
        loguru.logger.debug(f'添加了一行数据:{item_name} {brand} {price} {batch_serial_number} {quantity}')

    def _clear_all_table(self) -> None:
        ui = self.get_view()
        result = ui.show_mask_dialog(title='清空表格', content='确定要清空表格吗？')
        if result:
            ui.get_table_widget().clear()
            # 重新设置表格的Header
            ui.get_table_widget().setHorizontalHeaderLabels(self._table_headers)

    def _delete_current_row(self) -> None:
        ui = self.get_view()
        current_row = ui.get_table_widget().currentRow()
        if current_row == -1:
            ui.show_warning_infobar(title='没有选中任何行！', content='请选中要删除的行')
            return
        result = ui.show_mask_dialog(title='删除当前行', content='确定要删除当前行吗？')
        if result:
            ui.get_table_widget().removeRow(current_row)

    def _export_data_to_excel(self) -> None:
        """导出数据到Excel"""
        mask_title = '确认添加?'
        mask_content = '点击确认将会清空表格并将数据添加到数据库,在还没添加之前您可以在表格里面对数据双击进行修改'
        if not self.get_view().show_mask_dialog(title=mask_title, content=mask_content):
            return
        data = self._get_data()
        if not data:
            self.get_view().show_warning_infobar(title='没有数据！', content='请先添加数据')
            return
        self.get_model().export_data(data)
        self.get_view().show_success_infobar(title='导出成功！', content='数据已经成功导出到Excel和数据库中!',
                                             duration=-1)
        self.get_view().get_table_widget().clearContents()

    def _get_data(self) -> List[Tuple[str, str, float, str]]:
        """获取表格数据"""
        ui = self.get_view()
        table = ui.get_table_widget()
        row_count = table.rowCount()
        data = []

        for i in range(row_count):
            if self._is_row_empty(i):
                continue

            row_data = self._get_row_values(i)
            # 价格需要转换为float
            data.append((row_data[0], row_data[1], float(row_data[2]), row_data[3]))
        return data

    def _is_row_empty(self, row: int) -> bool:
        """判断某一行是否为空"""
        table = self.get_view().get_table_widget()
        for i in range(table.columnCount()):
            if table.item(row, i):
                return False
        return True

    def _get_row_values(self, row: int) -> list[str]:
        """获取某一行的值"""
        table = self.get_view().get_table_widget()
        values = []
        for i in range(table.columnCount()):
            values.append(table.item(row, i).text())
        return values

    def _connect_signals(self) -> None:
        ui = self.get_view()
        ui.get_confirm_button().clicked.connect(self._on_confirm_button_clicked)
        ui.get_clear_table_button().clicked.connect(self._clear_all_table)
        ui.get_delete_current_row_button().clicked.connect(self._delete_current_row)
        ui.get_save_table_button().clicked.connect(self._export_data_to_excel)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    storage_presenter = StoragePresenter()
    storage_presenter.get_view().show()
    app.exec()
