import pandas as pd

# 讀檔
df = pd.read_excel('xxx.xlsx')  # 替換成你的檔案名稱

# 欄位命名
df.columns = ['日期', '店櫃編號', '現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']
df['日期'] = df['日期'].astype(str)

# 加總總金額
df['總金額'] = df[['現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']].sum(axis=1)

# 各店總交易金額
total_by_store = df.groupby('店櫃編號')['總金額'].sum().reset_index()
print("👉 各店總交易金額")
print(total_by_store.head(10).to_string())

# 各店每月支付方式總和
monthly_by_store = df.groupby(['日期', '店櫃編號'])[
    ['現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']
].sum().reset_index()
print("\n👉 各店每月支付方式總和")
print(monthly_by_store.head(10).to_string())

# 各支付方式總體佔比
payment_sum = df[['現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']].sum()
payment_percent = (payment_sum / payment_sum.sum()) * 100
print("\n👉 各支付方式佔比 (%)")
print(payment_percent.round(2).to_string())

# 每筆找出最常用支付方式
df['最常用支付方式'] = df[['現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']].idxmax(axis=1)

# 每家店最常用支付方式
popular_method_by_store = df.groupby('店櫃編號')['最常用支付方式'].agg(lambda x: x.mode()[0]).reset_index()
print("\n👉 每家店最常用支付方式")
print(popular_method_by_store.to_string())
