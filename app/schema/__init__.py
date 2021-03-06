import mara_schema.config
from mara_app.monkey_patch import patch


@patch(mara_schema.config.data_sets)
def _data_sets():
    from app.schema.data_sets.order_items import order_items_data_set
    from app.schema.data_sets.sellers import sellers_data_set
    from app.schema.data_sets.customers import customers_data_set
    from app.schema.data_sets.products import products_data_set
    from app.schema.data_sets.leads import leads_data_set

    return [
        order_items_data_set,
        sellers_data_set,
        customers_data_set,
        products_data_set,
        leads_data_set
    ]
