from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class InventoryResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'cocktails', 'inventories'

    def get_by_inventory_id(self):
        sql = "SELECT inventory_id, inventory_name, ingredient_name, brand, measurement_qty, unit_name, abv, price " \
              "FROM (SELECT * FROM cocktails.inventories WHERE inventory_id = 1) AS a " \
              "JOIN cocktails.ingredients ON a.ingredient_id = ingredients.ingredient_id " \
              "JOIN cocktails.units ON a.unit_id = units.unit_id;"

        sql_res = RDBService.run_sql(sql, None, True)
        return sql_res

