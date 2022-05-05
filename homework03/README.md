Analyzing Turbidity Data
========================
This homework reads tubidity data from a json file and calculates turbidity, average turbidity, minimum time it takes for the turbidity to fall below a threshold, and determines if it is safe for use.

Downloading the Data
--------------------
To download the turbidity data, type `wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json` into the terminal.

How it Works
------------
1. The main function loops through each of the unique days and times and and reads in the calibration constant and detector current.

2. The function calculate_turbidity takes in parameters for the calibration constant and detector current and returns a float.

3. The function calculate_min_time takes in parameters for the turbidity threshold, current turbidity, and the decay factor and returns the minimum time it takes for the turbidity to fall below the treshold.

4. The function determine safe returns a bool that determines if the turbidity is safe or not.

5. The function calculate_avg_turbidity calculates current turbidity by averaging the previous 5 turbidities.

6. The program returns information about average turbidity, if the turbidity is above or below the threshold, and the minimum time.

Files
-----
1. `analyze_water.py` contains the functions that analyzes the data.

2. `test_analyze_water.py` contains unit tests for `analyze_water.py`.

Running the Code
----------------
1. Run the program by typing `python3 analyze_water.py` into the command line.

2. To run the unit tests, type `pytest test_analyze_water.py` into the command line.

Results
-------
The results will look like the following:  

Average turbidity based on most recent five measurements = 0.84 NTU  
INFO:root:Turbidity is above threshold for safe use  
Minimum time required to return below a safe threshold = 8.63 hours  

Where the first line is average turbidity, the second line is logging if the turbidity is safe, and the third line is the minimum time.

