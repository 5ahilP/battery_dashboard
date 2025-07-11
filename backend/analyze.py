def analyze_csv(df):
    try:
        result = {}

        # Basic stats
        result["voltage_avg"] = round(df["Voltage"].mean(), 2)
        result["current_avg"] = round(df["Current"].mean(), 2)
        result["temperature_max"] = round(df["Temperature"].max(), 2)
        result["cycle_count"] = int(df["Cycle_Count"].max())

        # Flags
        result["overheating"] = any(df["Temperature"] > 45)
        result["overvoltage"] = any(df["Voltage"] > 4.2)
        result["undervoltage"] = any(df["Voltage"] < 3.0)

        # Optional: Graphing-ready data
        result["graph"] = {
            "time": df["Time"].tolist(),
            "voltage": df["Voltage"].tolist(),
            "temperature": df["Temperature"].tolist()
        }

        return result
    except Exception as e:
        return {"error": str(e)}
