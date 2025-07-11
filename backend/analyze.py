def analyze_csv(df):
    # Just return basic info for now
    return {
        "columns": df.columns.tolist(),
        "rows": len(df)
    }
