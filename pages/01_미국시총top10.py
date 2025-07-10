import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 타이틀
st.title("📈 미국 시가총액 Top 10 기업 - 최근 3년간 주가 변동")

# 시가총액 Top 10 기업 (2025년 기준, 약간 변동 가능성 있음)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Amazon": "AMZN",
    "Meta Platforms": "META",
    "Alphabet (Class A)": "GOOGL",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY",
    "Tesla": "TSLA",
    "Broadcom": "AVGO"
}

# 날짜 범위 설정 (최근 3년)
end_date = datetime.today()
start_date = end_date - timedelta(days=3*365)

# 데이터 가져오기
st.sidebar.header("📊 주가 보기 설정")
selected_companies = st.sidebar.multiselect(
    "기업 선택 (기본값: 전체 선택)", 
    options=list(top10_tickers.keys()), 
    default=list(top10_tickers.keys())
)

st.sidebar.write("기간:", start_date.date(), " ~ ", end_date.date())

if selected_companies:
    fig = go.Figure()

    for name in selected_companies:
        ticker = top10_tickers[name]
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data['Adj Close'],
                mode='lines',
                name=name
            ))
        except Exception as e:
            st.error(f"{name} 데이터를 불러오는 중 오류 발생: {e}")

    fig.update_layout(
        title="최근 3년간 주가 변동 (Adjusted Close)",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        legend_title="기업",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("최소 한 개 이상의 기업을 선택해주세요.")
