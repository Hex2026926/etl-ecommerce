import pandas as pd
from sqlalchemy import create_engine

# 1. 读取清洗后的宽表
df = pd.read_csv('../data/orders_full_clean.csv')

# 2. 连接 MySQL
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/etl_ecommerce?charset=utf8mb4')

# 3. 写入 MySQL
df.to_sql('orders_full', engine, if_exists='replace', index=False)

# 4. 验证
result = pd.read_sql('SELECT COUNT(*) AS cnt FROM orders_full', engine)
print("入库行数：", result['cnt'][0])
print("数据入库完成！")