import streamlit as st
import pandas as pd
import pymongo
import webbrowser

# 连接到 MongoDB 数据库
client = pymongo.MongoClient('192.168.31.23', 27017)
db = client.pythondb
collection = db.ATop

results = collection.find()
df = pd.DataFrame(list(results))

df_show = df[['视频名', '博主', '播放量', '评论数']]
st.dataframe(df_show)
st.write('鼠标向右拖动🐾')

# buttonkey
num = 0

# 创建搜索框
search_box = st.text_input('请输入搜索关键词：')
#
# 标题 查询数据
if search_box:
    filtered_df = df[df['视频名'].str.contains(search_box, case=False)]
    st.write("共"+str(len(filtered_df))+'个视频')

    for row in filtered_df.iterrows():
        num += 1
        keys='button'+str(num)
        video_name = row[1]['视频名']
        web_value = df.loc[df['视频名'] == video_name, '网址'].values[0]
        st.image(row[1]['视频图片'], width=600)
        st.write('视频名：', row[1]['视频名'])
        st.write('UP主：', row[1]['博主'])
        if st.button('点击出现视频入口', key=keys):
            st.write('观看视频：', web_value)

# c1,c2=st.columns(2)
# with c1:
#     st.image(df.iloc[0]['视频图片'], width=200)
