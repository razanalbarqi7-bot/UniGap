import pandas as pd

# قراءة ملف البيانات
df = pd.read_csv("data/job_requirements.csv")
print(df.head())
print("Shape:", df.shape)
print(df.columns.tolist())

required_level = df["required_level"]
print("Average:", round(required_level.mean(), 1))
print("Highest:", required_level.max())
print("Lowest:", required_level.min())

# المهمة 3: عرض أول 5 صفوف لأعمدة job_id, skill_id, required_level
print(df[["job_id", "skill_id", "required_level"]].head(5))

# المهمة 4: متوسط وأعلى قيمة لعمود importance
print(df["importance"].mean())
print(df["importance"].max())