from gs_quant.data import Dataset
from gs_quant.session import GsSession
from datetime import date, timedelta

# 初始化 GS-Quant 会话
GsSession.use(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET")

# 定义日期范围
end_date = date.today()
start_date = end_date - timedelta(days=30)

# 获取股票数据
data_set = Dataset("US.STOCKS").get_data(
    instrument_id="AAPL", start_date=start_date, end_date=end_date
)

# 提取收盘价
close_prices = data_set["closePrice"]

# 计算简单移动平均线（SMA）
sma_window = 10  # 移动平均线窗口大小
sma = close_prices.rolling(window=sma_window).mean()

# 打印结果
print("股票数据:")
print(data_set)
print("\n简单移动平均线 (SMA):")
print(sma)
