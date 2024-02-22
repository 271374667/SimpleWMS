from src.dict_typing import (BatchCardDict, ItemQuantityCardDict, MoneyCardDict, StorageCardDict, WaveCardDict, RetrievalCardDict)
from src.model.home_model import HomeModel
from src.table_handler import TableHandler
from src.view.component_view.card_flyout_table_view import CardFlyoutTableView
from src.view.home_view import HomeView


class HomePresenter:
    def __init__(self):
        self._view = HomeView()
        self._model = HomeModel()
        self._flush_all_label()
        self._connect_signal()

    def get_view(self) -> HomeView:
        return self._view

    def get_model(self) -> HomeModel:
        return self._model

    def _current_batch_clicked(self) -> None:
        ui = self.get_view()
        current_batch_card = ui.get_current_batch_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, current_batch_card)
        self.current_batch_flyout.set_title('本月批次数据速览')
        self.current_batch_flyout.set_content('显示本月的批次数据,以及每一个批次一共有多少商品')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_show_headers(['批次序号', '创建时间', '商品数量'])
        current_batch_table_handler.set_headers(BatchCardDict)
        current_batch_table_handler.set_data(self.get_model().get_current_batch_card_data())
        self.current_batch_flyout.show_flyout()

    def _all_batch_clicked(self) -> None:
        ui = self.get_view()
        all_batch_card = ui.get_all_batch_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, all_batch_card)
        self.current_batch_flyout.set_title('全部批次数据速览')
        self.current_batch_flyout.set_content('显示所有的的批次数据,以及每一个批次一共有多少商品')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_show_headers(['批次序号', '创建时间', '商品数量'])
        current_batch_table_handler.set_headers(BatchCardDict)
        current_batch_table_handler.set_data(self.get_model().get_all_batch_card_data())
        self.current_batch_flyout.show_flyout()

    def _current_wave_clicked(self) -> None:
        ui = self.get_view()
        current_wave_card = ui.get_current_wave_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, current_wave_card)
        self.current_batch_flyout.set_title('本月波次数据速览')
        self.current_batch_flyout.set_content('显示本月的的波次数据,以及每一个波次一共有多少商品')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_show_headers(['波次序号', '创建时间', '商品数量'])
        current_batch_table_handler.set_headers(WaveCardDict)
        current_batch_table_handler.set_data(self.get_model().get_current_wave_card_data())
        self.current_batch_flyout.show_flyout()

    def _all_wave_clicked(self) -> None:
        ui = self.get_view()
        all_batch_card = ui.get_all_wave_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, all_batch_card)
        self.current_batch_flyout.set_title('全部波次数据速览')
        self.current_batch_flyout.set_content('显示所有的的波次数据,以及每一个波次一共有多少商品')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_show_headers(['波次序号', '创建时间', '商品数量'])
        current_batch_table_handler.set_headers(WaveCardDict)
        current_batch_table_handler.set_data(self.get_model().get_all_wave_card_data())
        self.current_batch_flyout.show_flyout()

    def _current_item_quantity_clicked(self) -> None:
        ui = self.get_view()
        current_item_quantity_card = ui.get_current_item_quantity_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, current_item_quantity_card)
        self.current_batch_flyout.set_title('本月商品数量速览')
        self.current_batch_flyout.set_content('显示本月的商品数量')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(ItemQuantityCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '商品数量'])
        current_batch_table_handler.set_data(self.get_model().get_current_item_quantity_card_data())
        self.current_batch_flyout.show_flyout()

    def _all_item_quantity_clicked(self) -> None:
        ui = self.get_view()
        all_item_quantity_card = ui.get_all_item_quantity_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, all_item_quantity_card)
        self.current_batch_flyout.set_title('全部商品数量速览')
        self.current_batch_flyout.set_content('显示所有的商品数量')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(ItemQuantityCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '商品数量'])
        current_batch_table_handler.set_data(self.get_model().get_all_item_quantity_card_data())
        self.current_batch_flyout.show_flyout()

    def _current_money_clicked(self) -> None:
        ui = self.get_view()
        current_money_card = ui.get_current_money_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, current_money_card)
        self.current_batch_flyout.set_title('本月商品金额速览')
        self.current_batch_flyout.set_content('显示本月的商品金额')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(MoneyCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '商品金额'])
        current_batch_table_handler.set_data(self.get_model().get_current_money_card_data())
        self.current_batch_flyout.show_flyout()

    def _all_money_clicked(self) -> None:
        ui = self.get_view()
        all_money_card = ui.get_all_money_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, all_money_card)
        self.current_batch_flyout.set_title('全部商品金额速览')
        self.current_batch_flyout.set_content('显示所有的商品金额')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(MoneyCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '商品金额'])
        current_batch_table_handler.set_data(self.get_model().get_all_money_card_data())
        self.current_batch_flyout.show_flyout()

    def _current_storage_clicked(self) -> None:
        ui = self.get_view()
        current_storage_card = ui.get_current_storage_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, current_storage_card)
        self.current_batch_flyout.set_title('本月商品入库信息速览')
        self.current_batch_flyout.set_content('显示本月的商品入库信息')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(StorageCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '入库数量'])
        current_batch_table_handler.set_data(self.get_model().get_current_storage_card_data())
        self.current_batch_flyout.show_flyout()

    def _all_storage_clicked(self) -> None:
        ui = self.get_view()
        all_storage_card = ui.get_all_storage_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, all_storage_card)
        self.current_batch_flyout.set_title('全部商品入库信息速览')
        self.current_batch_flyout.set_content('显示所有的商品入库信息')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(StorageCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '入库数量'])
        current_batch_table_handler.set_data(self.get_model().get_all_storage_card_data())
        self.current_batch_flyout.show_flyout()

    def _current_retrieval_clicked(self) -> None:
        ui = self.get_view()
        current_retrieval_card = ui.get_current_retrieval_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, current_retrieval_card)
        self.current_batch_flyout.set_title('本月商品出库信息速览')
        self.current_batch_flyout.set_content('显示本月的商品出库信息')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(RetrievalCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '出库数量'])
        current_batch_table_handler.set_data(self.get_model().get_current_retrieval_card_data())
        self.current_batch_flyout.show_flyout()

    def _all_retrieval_clicked(self) -> None:
        ui = self.get_view()
        all_retrieval_card = ui.get_all_retrieval_card()

        self.current_batch_flyout = CardFlyoutTableView(ui, all_retrieval_card)
        self.current_batch_flyout.set_title('全部商品出库信息速览')
        self.current_batch_flyout.set_content('显示所有的商品出库信息')
        current_batch_table_handler = TableHandler(self.current_batch_flyout.table)
        current_batch_table_handler.set_headers(RetrievalCardDict)
        current_batch_table_handler.set_show_headers(['商品名称', '商品品牌', '出库数量'])
        current_batch_table_handler.set_data(self.get_model().get_all_retrieval_card_data())
        self.current_batch_flyout.show_flyout()

    def _flush_all_label(self) -> None:
        ui = self.get_view()
        ui.get_current_batch_label().setText(self.get_model().get_current_batch_name())
        ui.get_current_wave_label().setText(self.get_model().get_current_wave_name())
        ui.get_current_item_quantity_label().setText(str(self.get_model().get_current_item_quantity()))
        ui.get_current_money_label().setText(str(self.get_model().get_current_money()))
        ui.get_current_storage_label().setText(str(self.get_model().get_current_storage()))
        ui.get_current_retrieval_label().setText(str(self.get_model().get_current_retrieval()))
        ui.get_all_batch_label().setText(str(self.get_model().get_all_batch_number()))
        ui.get_all_wave_label().setText(str(self.get_model().get_all_wave_number()))
        ui.get_all_item_quantity_label().setText(str(self.get_model().get_all_item_quantity()))
        ui.get_all_money_label().setText(str(self.get_model().get_all_money()))
        ui.get_all_storage_label().setText(str(self.get_model().get_all_storage()))
        ui.get_all_retrieval_label().setText(str(self.get_model().get_all_retrieval()))

    def _flush_button_clicked(self) -> None:
        self._flush_all_label()
        self.get_view().show_success_infobar("刷新成功", '所有的数据都已经刷新成功了哦~', 5000)

    def _connect_signal(self):
        ui = self.get_view()
        ui.get_flush_tool_button().clicked.connect(self._flush_button_clicked)

        # 设置卡片点击
        ui.get_current_batch_card().clicked.connect(self._current_batch_clicked)
        ui.get_all_batch_card().clicked.connect(self._all_batch_clicked)
        ui.get_current_wave_card().clicked.connect(self._current_wave_clicked)
        ui.get_all_wave_card().clicked.connect(self._all_wave_clicked)
        ui.get_current_item_quantity_card().clicked.connect(self._current_item_quantity_clicked)
        ui.get_all_item_quantity_card().clicked.connect(self._all_item_quantity_clicked)
        ui.get_current_money_card().clicked.connect(self._current_money_clicked)
        ui.get_all_money_card().clicked.connect(self._all_money_clicked)
        ui.get_current_storage_card().clicked.connect(self._current_storage_clicked)
        ui.get_all_storage_card().clicked.connect(self._all_storage_clicked)
        ui.get_current_retrieval_card().clicked.connect(self._current_retrieval_clicked)
        ui.get_all_retrieval_card().clicked.connect(self._all_retrieval_clicked)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    main_presenter = HomePresenter()
    main_presenter.get_view().show()
    app.exec()
