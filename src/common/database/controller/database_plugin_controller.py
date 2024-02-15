from datetime import datetime

from src.common.database.service.get_attribute_service import GetAttributeService


class DatabasePluginController:
    def __init__(self):
        self._get_attribute_service = GetAttributeService()

    def get_unsalable_data(self):
        """获取滞销数据
        Returns:
            list[Tuple]: 滞销数据
                [(物品名称, 品牌, 批次, 在仓库中停留的天数, 存货数量, 总共进货, 存货率)]
        """
        total_data_after_group = self._get_attribute_service.get_all_inventory_and_count_group_by_batch_brand_name()
        unsold_data_after_group = self._get_attribute_service.get_unsold_inventory_and_count_group_by_batch_brand_name()
        today = datetime.today()

        # 根据未销售的数据进行计算
        unsold_data = []
        for unsold in unsold_data_after_group:
            for total in total_data_after_group:
                if unsold[0] == total[0] and unsold[1] == total[1] and unsold[2] == total[2]:
                    # 获取在仓库中停留的天数
                    stay_days = (today.date() - total[3].date()).days
                    unsold_data.append(
                            (unsold[0],
                            unsold[1],
                            unsold[2],
                            stay_days,
                            unsold[4],
                            total[4],
                            round((unsold[4] / total[4]), 6) * 100))
                    continue
        return unsold_data

    # 脱销的逻辑一样，这里直接偷懒
    get_out_of_stock_data = get_unsalable_data


if __name__ == '__main__':
    d = DatabasePluginController()
    print(d.get_unsalable_data())
