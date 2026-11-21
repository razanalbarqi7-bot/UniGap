import pandas as pd

# المهام 1 و 2: قراءة الملف ومعالجة القيم المفقودة بالوسيط (Median)
df = pd.read_csv("data/UniGap_edge_cases.csv")

print(df)
print("Missing levels:", df["level"].isna().sum())
df["level"] = df["level"].fillna(df["level"].median())
print(df)

# المهمة 3: إزالة الصفوف المكررة
df = df.drop_duplicates()

# المهمة 4: الاحتفاظ فقط بالمستويات من 0 إلى 100
df = df[(df["level"] >= 0) & (df["level"] <= 100)]

print(df)