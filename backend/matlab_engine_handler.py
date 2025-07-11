import matlab.engine

# Start MATLAB Engine once globally for efficiency
eng = matlab.engine.start_matlab()

def analyze_in_matlab(voltage, current, time, temp):
    voltage_mat = matlab.double(voltage)
    current_mat = matlab.double(current)
    time_mat = matlab.double(time)
    temp_mat = matlab.double(temp)

    result = eng.analyze_battery(voltage_mat, current_mat, time_mat, temp_mat, nargout=1)
    
    # Return result as Python dict
    return {
        'soc': result['soc'],
        'soh': result['soh'],
        'temp': result['temp'],
        'time': result['time']
    }