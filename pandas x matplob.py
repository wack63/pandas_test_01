import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc('font', family='Microsoft JhengHei')
# 假設已有 df 變數，這裡模擬一份格式相同的 DataFrame（若實作請替換為實際的 Excel 匯入）
df = pd.read_excel('小拉基.xlsx')  # 實際使用時

# 欄位命名範例
columns = ['日期', '店櫃編號', '現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']
# 為了示範，這裡用隨機數據生成簡易資料（實際使用時用你的資料）
# 資料省略生成部分，使用者原本已載入 df

# 這裡執行分析：重新整理資料格式
df['日期'] = df['日期'].astype(str)
df['總金額'] = df[['現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']].sum(axis=1)

# 資料樞紐表：以「店鋪編號」為 index、「月份」為欄位，顯示總金額
pivot_table = df.pivot_table(index='店櫃編號', columns='日期', values='總金額', aggfunc='sum').fillna(0)

# 🔷 視覺化 1：每店鋪每月總金額熱力圖
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_table, cmap='YlGnBu', linewidths=.5)
plt.title("各店鋪每月交易總金額熱力圖", fontsize=16)
plt.xlabel("月份")
plt.ylabel("店櫃編號")
plt.tight_layout()
plt.show()

# 🔷 視覺化 2：各支付方式的每月總和趨勢圖
monthly_totals = df.groupby('日期')[['現金', '連線信用卡', '離線信用卡', 'LINE_PAY', '全支付PAY', '台灣PAY']].sum()

plt.figure(figsize=(14, 6))
for column in monthly_totals.columns:
    plt.plot(monthly_totals.index, monthly_totals[column], marker='o', label=column)
plt.title("各支付方式每月交易金額趨勢", fontsize=16)
plt.xlabel("月份")
plt.ylabel("金額")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
