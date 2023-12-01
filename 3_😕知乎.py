import streamlit as st
import pymongo
import pandas as pd


st.markdown("<h1 style='text-align: center;'>知乎热点周榜</h1>", unsafe_allow_html=True)
# 连接到 MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["zh_top"]
collection_quest = db["top_quest"]
collection_react = db['top_react']

# 查询数据并转换为 DataFrame
data_quest = list(collection_quest.find())
data_react = list(collection_react.find())
df = pd.DataFrame(data_quest)
df_react = pd.DataFrame(data_react)
# 处理关键字
df['标签'] = df['topics'].apply(lambda x: [topic['name'] for topic in x])

df = df.rename(columns={'title': '标题'})
df_react = df_react.rename(
    columns={'follow_num': '关注量', 'answer_num': '回答量', 'upvote_num': '赞同量', 'pv': '浏览量'})
# 获取quest的数据
df_data = df[['标题', '标签', 'url', 'num']]
# 获取reaction里面的数据
df_react = df_react[['关注量', '浏览量', '回答量', '赞同量', 'num']]
#拼接
df_con = pd.merge(df_data, df_react, on='num', how='inner')
#改顺序
new_order = ['标题', '标签', '关注量', '浏览量', '回答量', '赞同量', 'url', 'num']
df_con = df_con.reindex(columns=new_order)

height = 600
width = 2500
st.dataframe(df_con, height=height, width=width)
st.write('鼠标向右拖动🐾')

url = df['url']


