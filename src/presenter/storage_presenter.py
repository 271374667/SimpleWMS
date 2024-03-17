import loguru

from src.dict_typing import ReStorageDict, StorageDict
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

        # 设置自动波次开关默认开启
        self.get_view().get_auto_switch_button().setChecked(True)

    def get_view(self) -> StorageView:
        return self._view

    def get_model(self) -> StorageModel:
        return self._model

    def _on_confirm_button_clicked(self) -> None:
        """确认按钮点击事件,将数据添加到表格中"""
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
                        'price': price,
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
                    "price": price,
                    "batch_serial_number": batch_serial_number
                    }
            new_data_list.append(new_data)
        self._table_handler.add_rows(new_data_list)
        loguru.logger.debug(f'添加了一行数据:{item_name} {brand} {price} {batch_serial_number} {quantity}')

    def _on_return_mode_switch_btn_clicked(self) -> None:
        """切换模式按钮点击事件"""
        # 清空表格所有内容,并给出提示
        current_mode = self.get_view().get_return_switch_button().isChecked()
        if current_mode is True and self.get_view().show_mask_dialog(
                title='确定要切换模式吗?',
                content='如果您切换模式,'
                        '表格中的所有数据将会被清空且无法恢复,'
                        '同时在该模式下请您不要编辑表格数据'
                        '请您在进行操作前先确认!',
                ):
            self._table_handler.clear()
            self.get_view().show_success_infobar(title='切换模式成功!', content='当前模式已经切换为退货模式')
            self._table_handler.set_headers(ReStorageDict)
            self._table_handler.set_show_headers(
                    ['名称', '品牌', '价格', '入库时间', '退货次数', '批次号', '波次号', 'EAN13'])
            loguru.logger.debug('切换模式成功!')
            return

        # 切换模式需要更改一些属性,下面为退出退货模式
        self.get_view().get_return_switch_button().setChecked(False)
        self._table_handler.clear()
        self._table_handler.set_headers(StorageDict)
        self._table_handler.set_show_headers(['名称', '品牌', '价格', '批次号'])

        if current_mode is False:
            self.get_view().show_info_infobar(title='取消切换模式', content='您已经取消了切换模式的操作')

    def _on_return_lineedit_enter(self) -> None:
        """退货按钮文本框按下回车事件"""
        ui = self.get_view()
        current_text = ui.get_return_lineedit().text()
        if not current_text:
            ui.show_warning_infobar(title='输入内容错误', content='您当前没有输入任何内容,请检查您的输入')
            return

        # 检查是否是数字
        if not current_text.isdigit():
            self.get_view().show_warning_infobar(title='输入类型错误', content='输入必须为数字')
            return

        # 检查是否是 EAN13 格式
        if not self.get_model().is_real_ean13(current_text):
            ui.show_warning_infobar(title='输入格式错误', content='您输入的不是标准的EAN13,请检查您的输入')
            return

        # 检查是否是已经出库的商品
        if not self.get_model().is_inventory_sold(current_text):
            ui.show_warning_infobar(title='输入商品出错', content='您输入的商品未出库或者不存在,请检查您的输入')
            return

        # 判断当前数据是否已经存在于表格中
        for row in range(ui.get_table_widget().rowCount()):
            if self._table_handler.is_null(row):
                break
            elif current_text == ui.get_table_widget().item(row, 7).text():
                ui.show_warning_infobar(title='商品已经存在',
                                        content=f'EAN13为{current_text}的商品在表格中已经存在,不要重复添加')
                return

        # 将数据添加到表格中
        row_data = self.get_model().get_inventory_by_ean13(current_text)
        self._table_handler.add_row(row_data)
        loguru.logger.debug(f'添加了一行数据:{row_data}')
        ui.get_return_lineedit().clear()
        ui.show_success_infobar(title='添加成功', content='已经成功添加了一行数据')

    def _clear_all_table(self) -> None:
        ui = self.get_view()

        if ui.show_mask_dialog(title='清空表格', content='确定要清空表格吗？'):
            self._table_handler.clear()
            loguru.logger.debug('清空了表格')

    def _delete_current_row(self) -> None:
        ui = self.get_view()
        current_row = ui.get_table_widget().currentRow()
        if current_row == -1:
            ui.show_warning_infobar(title='没有选中任何行！', content='请选中要删除的行')
            return

        if ui.show_mask_dialog(title='删除当前行', content='确定要删除当前行吗？'):
            ui.get_table_widget().removeRow(current_row)
            loguru.logger.debug(f'删除了一行数据:{current_row}')

    def _export_mode_factory(self) -> None:
        """通过判断当前模式来执行不同的导出操作"""
        if self.get_view().get_return_switch_button().isChecked():
            self._export_return_data_to_excel()
            return
        self._export_normal_data_to_excel()

    def _export_normal_data_to_excel(self) -> None:
        """导出数据到Excel"""
        data: list[StorageDict] = self._table_handler.get_data()
        if not data:
            self.get_view().show_warning_infobar(title='没有数据！', content='请先添加数据')
            return

        mask_title = '确认添加?'
        mask_content = '点击确认将会清空表格并将数据添加到数据库,在还没添加之前您可以在表格里面对数据双击进行修改'
        if not self.get_view().show_mask_dialog(title=mask_title, content=mask_content):
            return

        def run_func():
            self.get_model().export_data(data)

        def finish_func():
            self.get_view().finish_state_tooltip()
            loguru.logger.debug('状态提示框已经关闭')
            self.get_view().show_success_infobar(title='导出成功！', content='数据已经成功导出到Excel和数据库中!',
                                                 duration=-1)
            self._table_handler.clear()
            loguru.logger.info('导出了数据到Excel和数据库')

        self._run_in_thread = RunInThread()
        self._run_in_thread.set_start_func(run_func)
        self._run_in_thread.set_finished_func(finish_func)
        self._run_in_thread.start()
        save_btn_pos = self.get_view().get_save_table_button().frameGeometry().topLeft()
        loguru.logger.debug(f'显示状态提示框在如下位置:{save_btn_pos}')
        self.get_view().show_state_tooltip('正在导出数据',
                                           '请稍等...')

    def _export_return_data_to_excel(self) -> None:
        data: list[ReStorageDict] = self._table_handler.get_data()
        if not data:
            self.get_view().show_warning_infobar(title='没有数据！', content='请先添加数据')
            return

        mask_title = '确认添加?'
        mask_content = '点击确认将会清空表格并将退货数据修改同步至数据库'
        if not self.get_view().show_mask_dialog(title=mask_title, content=mask_content):
            return

        def run_func():
            self.get_model().export_return_data(data)

        def finish_func():
            self.get_view().finish_state_tooltip()
            loguru.logger.debug('状态提示框已经关闭')
            self.get_view().show_success_infobar(title='修改成功！', content=f'{len(data)}条数据已经成功同步至数据库中!',
                                                 duration=-1)
            self._table_handler.clear()
            loguru.logger.info(f'修改了{len(data)}条退货数据到数据库中')

        self._run_in_thread = RunInThread()
        self._run_in_thread.set_start_func(run_func)
        self._run_in_thread.set_finished_func(finish_func)
        self._run_in_thread.start()
        save_btn_pos = self.get_view().get_save_table_button().frameGeometry().topLeft()
        loguru.logger.debug(f'显示状态提示框在如下位置:{save_btn_pos}')
        self.get_view().show_state_tooltip('正在导出数据',
                                           '请稍等...')

    def _connect_signals(self) -> None:
        ui = self.get_view()
        ui.get_confirm_button().clicked.connect(self._on_confirm_button_clicked)
        ui.get_clear_table_button().clicked.connect(self._clear_all_table)
        ui.get_delete_current_row_button().clicked.connect(self._delete_current_row)
        ui.get_delete_current_row_button().clicked.connect(
                lambda: self.get_view().finish_state_tooltip('成功!', '清除完成'))
        ui.get_save_table_button().clicked.connect(self._export_mode_factory)
        ui.get_return_switch_button().checkedChanged.connect(self._on_return_mode_switch_btn_clicked)
        ui.get_return_lineedit().returnPressed.connect(self._on_return_lineedit_enter)
        ui.get_return_pushbutton().clicked.connect(self._on_return_lineedit_enter)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])

    storage_presenter = StoragePresenter()
    storage_presenter.get_view().show()
    app.exec()
