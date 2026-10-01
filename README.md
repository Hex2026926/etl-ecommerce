# ETL E-commerce

## 项目简介
从多个 CSV 抽取电商数据（订单、客户、商品、明细、评论），用 Python 清洗、多表关联后入库 MySQL，并用 SQL 做电商分析。

## 技术栈
- Python 3.8
- pandas
- MySQL 8.0

## 项目结构
- data/         原始数据 + 清洗后宽表
- scripts/      探索 + 清洗 + 入库脚本
- sql/          分析查询

## 怎么运行
1. 安装依赖：pip install -r requirements.txt
2. 探索数据：python scripts/explore.py
3. 运行入库脚本：python scripts/load.py
4. 执行 SQL 查询：source sql/analysis.sql

## 成果
- 清洗了 500 行订单数据
- 完成 6 条 SQL 分析查询
- 总订单数：185
- 总客户数：88
- 总销售额：1,143,285.63
- 支付方式 Top1：PayPal（53 单）
- 商品类别 Top1：Books（108,409.65）
- 消费最高客户：Carol Lawson（70,296.61）