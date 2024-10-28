import plotly.express as px
df = px.data.iris()
print(df.head())
'''
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="species", # Species 열의 값에 따라서 색깔 표현
                 size='petal_length', # petal_length 에 따라 크기를 변화
                 hover_data=['petal_width'], # 참고할 데이터 추가
                 title='Iris Data - Scatter Plot' # 그래프 타이틀 지정
                )
fig.show()
'''
'''
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter( # x축 값을 생략한 경우 DataFrame의 Index에 의해 배치됨
    y = df['sepal_length'], # y축 값 sepal_length 값에 따라 배치
    mode='markers', # Scatter Plot을 그리기 위해 Markers
    marker=dict(    # Marker에 대한 세부적은 설정을 지정
        size=20,    # 점 크기
        color=df['petal_length'], # 색깔 값을 petal_length에 따라 변하도록 설정
        colorscale='Viridis', # one of plotly colorscales
        showscale=True,  # colorscales 보여줌
        line_width=1, # 마커 라인 두께 설정
    )
))
fig.update_layout(title='Iris Data')
fig.show()
'''