import streamlit as st
import requests
from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量中读取
BOT_ID = os.getenv("BOT_ID")
API_KEY = os.getenv("API_KEY")