def clean_data(df):
    df["level"] = df["level"].fillna(df["level"].median())
    df = df.drop_duplicates()
    df = df[(df["level"] >= 0) & (df["level"] <= 100)]
    return df
