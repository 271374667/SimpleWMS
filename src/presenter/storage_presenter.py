from typing import List, Tuple

from src.model.storage_model import StorageModel
from src.view.storage_view import StorageView


class StoragePresenter:
    def __init__(self):
        self._data: List[Tuple[str, str, float, int]] = []
        self._view = StorageView()
        self._model = StorageModel()
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
            self.get_view().add_table_row(item_name, brand, price, self.get_model().gen_batch_serial_number(batch),
                                          quantity)
            return

        # 如果是自动切换，那么就需要先获取最新的批次
        batch_serial_number = self.get_model().get_newest_batch_serial_number()
        self.get_view().add_table_row(item_name, brand, price, batch_serial_number, quantity)

    def _clear_all_table(self) -> None:
        ui = self.get_view()
        result = ui.show_mask_dialog(title='清空表格', content='确定要清空表格吗？')
        if result:
            ui.get_table_widget().clear()
            # 重新设置表格的Header
            ui.get_table_widget().setHorizontalHeaderLabels(['商品名称', '品牌', '价格', '批次'])
            self._data.clear()

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
        data = self._get_data()
        self.get_model().export_data(data)
        self.get_view().show_success_infobar(title='导出成功！', content='数据已经成功导出到Excel和数据库中!', duration=-1)
        self.get_view().get_table_widget().clearContents()

    def _get_data(self) -> List[Tuple[str, str, str, str]]:
        """获取表格数据"""
        ui = self.get_view()
        table = ui.get_table_widget()
        row_count = table.rowCount()
        data = []
        for i in range(row_count):
            # 如果某一行的数据不完整，那么就跳过这一行
            if (not table.item(i, 0)
                    or not table.item(i, 1)
                    or not table.item(i, 2)
                    or not table.item(i, 3)):
                continue
            item_name = table.item(i, 0).text()
            brand = table.item(i, 1).text()
            price = table.item(i, 2).text()
            batch = table.item(i, 3).text()
            data.append((item_name, brand, price, batch))
        print(data)
        return data

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
