import logging
import json
import numpy as np
import math

logging.basicConfig(level = logging.DEBUG)

def calculate_turbidity(a0: float, I90: float) -> float:
    """Calculates turbidity.

    Calculates the value of turbidity given the calibration constant and ninety degree detector current.

    Args:
        a0 (float): Value of the calibration constant.
        I90 (float): Value of the ninety degree detector current.

    Returns:
        A float value that represents turbidity given calibration constant and ninety degree detector current.
    """
    T = a0 * I90
    return abs(T)


def calculate_min_time(Ts: float, T0: float, d: float) -> float:
    """Calculates minimum time to fall below threshold turbidity.

    Calculates the value of the minimum time it takes to fall below the turbidity threshold, given the turbidity threshold for safe water, the current turbidity, the decay factor per hour, and hours elapsed.

    Args:
        Ts (float): Value of the turbidity threshold for safe water.
        T0 (float): Value of the current turbidity.
        d (float): Value for the decay factor per hour  expressed as a decimal.

    Returns:
        A float value that represents the minimum time it takes go fall below the turbidity threshold given the turbidity threshold for safe water, current turbidity, decay facor per hour, and hours elapsed.
    """
 
    ret = math.log((Ts/T0), float(1-d))
    return abs(ret)


def determine_safe(Ts: float, T0: float) -> str:
    """Determines if the turbidity is above threshold for safe use.
    
    Uses an inequality to check if the turbidity is above the threshold for safe use given the threshold and current turbidity.

    Args: 
        Ts (float): Value of the turbidity threshold for safe water.
        T0 (float): Value of the current turbidity.

    Returns:
        A bool that returns false if the turbidity is above the treshold for safe use and true if it is below the threshold for safe use.
    """

    return(T0 < Ts)
    

def calculate_avg_turbidity(turbidities: list) -> list:
    """Calculates the turbidity using average of 5 previous points.

    Calculates the current turbidity by using the average of the past 5 turbidities and puts it into a list.

    Args:
        turbidities (list): List that holds the current turbidities calculated from calibration constant and detector current.

    Returns:
        A list that contains the average of the past 5 turbidities.
    """
    average_turbidity = 0
    average_turbidity_list = []
 
    for index in range(0,len(turbidities)-1):
        average_turbidity_list.append(index)

    average_turbidity_list[0] = turbidities[0]

    for i in range(1, len(turbidities)-1):
        if(i < 5):
            for j in range(0, i):
                average_turbidity = average_turbidity + turbidities[i]
            average_turbidity_list[i] = round(average_turbidity/(i+1), 4)
            average_turbidity = 0

        else:
            for j in range(j-5, j-1):
                average_turbidity = average_turbidity +turbidities[i]
            average_turbidity_list[i] = round(float(average_turbidity/5), 4)
            average_turbidity = 0

    return average_turbidity_list

    
def main():

    count = 0

    with open('turbidity_data.json', 'r') as f:
        turbidity_data_file = json.load(f)

    Ts = 1.0
    d = 0.02

    turbidity_list = []
    calibration_constant_list = []
    detector_current_list = []

    for i in turbidity_data_file['turbidity_data']:

        calibration_constant = turbidity_data_file['turbidity_data'][count]['calibration_constant']
        calibration_constant_list.append(calibration_constant)

        detector_current = turbidity_data_file['turbidity_data'][count]['detector_current']
        detector_current_list.append(detector_current)

        turbidity_list.append(calculate_turbidity(calibration_constant, detector_current))

        
        count = count+1       

    average_turbidity_list = calculate_avg_turbidity(turbidity_list)

    for r in range(0, len(turbidity_list)-1):
        print('Average turbidity based on most recent five measurements = ' + str(average_turbidity_list[r]) + ' NTU')
      
        if(determine_safe(Ts, average_turbidity_list[r])):
            logging.info('Turbidity is above threshold for safe use')
        else:
            logging.warning('Turbidity is above threshold for safe use')
        print('Minimum time required to return below a safe threshold = ' + str(round(calculate_min_time(Ts, average_turbidity_list[r], d), 2)) + ' hours')
 
if __name__ == '__main__':
    main()


 
