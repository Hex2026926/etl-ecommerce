import pandas as pd

# 读取五张表
customers = pd.read_csv('../data/customers.csv')
orders = pd.read_csv('../data/orders.csv')
order_items = pd.read_csv('../data/order_items.csv')
products = pd.read_csv('../data/products.csv')
reviews = pd.read_csv('../data/product_reviews.csv')

# 查看每张表的形状和列名
print("=== customers ===")
print("形状：", customers.shape)
print("列名：", customers.columns.tolist())

print("\n=== orders ===")
print("形状：", orders.shape)
print("列名：", orders.columns.tolist())

print("\n=== order_items ===")
print("形状：", order_items.shape)
print("列名：", order_items.columns.tolist())

print("\n=== products ===")
print("形状：", products.shape)
print("列名：", products.columns.tolist())

print("\n=== reviews ===")
print("形状：", reviews.shape)
print("列名：", reviews.columns.tolist())

# 验证关联字段
print("=== 验证关联字段 ===")
print("customers 主键：", customers['customer_id'].nunique(), "个唯一值")
print("orders 外键：", orders['customer_id'].nunique(), "个唯一值")
print("orders 主键：", orders['order_id'].nunique(), "个唯一值")
print("order_items 外键：", order_items['order_id'].nunique(), "个唯一值")
print("order_items 商品外键：", order_items['product_id'].nunique(), "个唯一值")
print("products 主键：", products['product_id'].nunique(), "个唯一值")
print("reviews 客户外键：", reviews['customer_id'].nunique(), "个唯一值")
print("reviews 商品外键：", reviews['product_id'].nunique(), "个唯一值")

# 多表关联：订单 + 订单明细 + 商品 + 客户
# 1. 订单 + 客户
orders_customers = pd.merge(orders, customers, on='customer_id', how='left')
print("orders + customers 形状：", orders_customers.shape)

# 2. 再关联订单明细
orders_items = pd.merge(orders_customers, order_items, on='order_id', how='left')
print("orders + customers + order_items 形状：", orders_items.shape)

# 3. 再关联商品
full_data = pd.merge(orders_items, products, on='product_id', how='left')
print("完整宽表形状：", full_data.shape)

# 4. 查看前几行
print("\n宽表前5行：")
print(full_data.head())

# 5. 保存宽表
full_data.to_csv('../data/orders_full.csv', index=False)
print("\n宽表已保存到 data/orders_full.csv")

# 检查宽表的缺失值
print("=== 宽表缺失值 ===")
print(full_data.isnull().sum())

# 检查宽表重复值
print("\n宽表重复行数：", full_data.duplicated().sum())

# 查看宽表的列名
print("\n宽表列名：")
print(full_data.columns.tolist())

# 删除没有明细的订单（空订单）
full_data = full_data.dropna(subset=['product_id'])
print("删除空订单后形状：", full_data.shape)

# 保存清洗后的宽表
full_data.to_csv('../data/orders_full_clean.csv', index=False)
print("清洗后宽表已保存到 data/orders_full_clean.csv")

# 再次验证
print("\n清洗后缺失值：")
print(full_data.isnull().sum())