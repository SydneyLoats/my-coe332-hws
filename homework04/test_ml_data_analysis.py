from ml_data_analysis import*

import math
import pytest

def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

def test_compute_average_mass_exceptions():
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')                               # send an empty list
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')             # dictionaries not uniform
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')           # value not a float
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')             # key not in dicts

def test_check_hemisphere():
    assert check_hemisphere(1, 1) == 'Northern & Eastern'
    assert check_hemisphere(1, -1) == 'Northern & Western'
    assert check_hemisphere(-1, 1) == 'Southern & Eastern'
    assert check_hemisphere(-1, -1) == 'Southern & Western'
    assert isinstance(check_hemisphere(1, 1), str) == True

def test_check_hemisphere_exceptions():
    with pytest.raises(TypeError):                                  # value not a float
        check_hemisphere('a', 1)
    with pytest.raises(TypeError):                                  # value not a float
        check_hemisphere(1, 'a')                                    

def test_count_classes():
    assert isinstance(count_classes([{'a': 10}, {'a': 2}], 'a'), dict) == True
    assert count_classes({}, 'a') == {}

def test_count_classes_exceptions():
    with pytest.raises(TypeError):
        count_classes(1, 'a')                                       # value not a dict
    with pytest.raises(KeyError):
        count_classes([{'a': 1}, {'a': 2}], 'b')                    # key not in dicts
    with pytest.raises(KeyError):
        count_classes([{'a': 1}, {'b': 1}], 'a') == [1]             
