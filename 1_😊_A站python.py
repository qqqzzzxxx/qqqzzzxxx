import streamlit as st
import pymongo
# 连接到 MongoDB 数据库
client = pymongo.MongoClient('localhost', 27017)
db = client.pythondb
collection = db.PY_data
# 显示数据
results = collection.find()
st.table(results)