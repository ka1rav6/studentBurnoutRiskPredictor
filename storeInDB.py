import pandas as pd
from pymongo import MongoClient
import json
import pandas as pd

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
db = client["student_burnout"]
collection = db["studentDetails"]


df = pd.read_csv("student_mental_health_burnout_1M.csv") #from kaggle
df = df.drop_duplicates()
df = df.dropna()
df.to_json("student_file.json", orient="records", indent=2)
with open("student_file.json", "r") as f:
    file_data = json.load(f)
collection.insert_many(file_data)