import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Group by
    # Only Feb 2020
    feb_orders = orders[(orders.order_date.dt.month == 2) & (orders.order_date.dt.year == 2020)]
    sum_of_feb_orders = feb_orders.groupby('product_id')[['unit']].sum()
    df = products.merge(sum_of_feb_orders, on='product_id')
    return df[df.unit >= 100][['product_name', 'unit']]