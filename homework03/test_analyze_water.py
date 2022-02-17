from analyze_water import*

import math
import pytest

with open('turbidity_data.json', 'r') as f:
    turbidity_data_file = json.load(f)

calibration = '0.987'

def test_calc_turbidity():
    
    a0, I90 = calculate_turbidity(calibration, turbidity_data_file)

    assert isinstance(a0, float)
    assert isinstance(I90, float)
    assert calculate_turbidity(0, 0) == 0
    assert calculate_turbidity(1, 2) == 2
    with pytest.raises(TypeError):
        calculate_turbidity(True, False)


Ts = 1.0
d = 0.02
T0 = calculate_turbidity(calibration, turbidity_data_file)

def test_calc_min_time():

    assert isinstance(Ts, float)
    assert isinstance(T0, float)
    assert isinstance(d, float)
    assert calculate_min_time(1, 0.5, .02) == math.log((1/0.5), (1-.02))
    with pytest.raises(TypeError):
        calculate_min_turbidity(True, False)
