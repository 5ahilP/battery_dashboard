import numpy as np
from matlab_engine_handler import analyze_in_matlab

def analyze_csv(df):
    # Basic checks
    required_columns = ['Time', 'Voltage', 'Current', 'Temp']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV must contain Time, Voltage, Current, Temp columns")

    # Convert to lists
    time = df['Time'].tolist()
    voltage = df['Voltage'].tolist()
    current = df['Current'].tolist()
    temp = df['Temp'].tolist()

    # Call MATLAB
    matlab_result = analyze_in_matlab(voltage, current, time, temp)

    # Format output
    soc = matlab_result['soc'][0] if isinstance(matlab_result['soc'], list) else matlab_result['soc']
    soh = matlab_result['soh']

    return {
        "SoC": soc,
        "SoH": soh,
        "Temp": temp,
        "Time": time
    }