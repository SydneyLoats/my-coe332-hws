#Sydney Loats SML4267 homework03



#This homework reads tubidity data from a json file and calculates turbidity, average turbidity, minimum time it takes for the turbidity to fall below a threshold, and determines if it is safe for use



#To download the json file and use it to run the program,

##STEP 1: 

##Go to this link

##   https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

##Press ctrl-s and save the json file to somewhere in your computer.

##For example, I saved mine to \Users\sydney\Documents\UT\2022Spring\COE332

##The file should be named turbidity_data.json

###STEP 2:

###Open the command prompt on your computer and navigate to the directory where turbidity_data.json is located.

###It should look similar to the following:

###C:\Users\sydney\Documents\UT\2022Spring\COE311k> 

###The use secure copy, scp, to copy the file to your isp02 computer. It should look similar to the following (use your own username, I'm using sloats"

###C:\Users\sydney\Documents\UT\2022Spring\COE311k>scp tubidity_data.json sloats@isp.tacc.utexas.edu:

###The json file will be copied to your isp computer and you should move the file into the folder where the other .py files required to run the program are located




#This homework reads tubidity data from a json file and calculates turbidity, average turbidity, minimum time it takes for the turbidity to fall below a threshold, and determines if it is safe for use

##The main function loops through each of the unique days and times and and reads in the calibration constant and detector current.

##The function calculate_turbidity takes in parameters for the calibration constant and detector current and returns a float.

##The function calculate_min_time takes in parameters for the turbidity threshold, current turbidity, and the decay factor and returns the minimum time it takes for the turbidity to fall below the treshold

##The function determine safe returns a bool that determines if the turbidity is safe or not.

##The function calculate_avg_turbidity calculates current turbidity by averaging the previous 5 turbidities.

##The program returns information about average turbidity, if the turbidity is above or below the threshold, and the minimum time.




##The test_analyze_water.py file contains unit tests for analyze_water.py



#To run the complete program, first download the turbidity data using the steps to download the json file. Then run the program by typing 

#python3 analyze_water.py

#into the command line.

##The first line will display average turbidity.

##The second line will be a logging of if the turbidity is safe

##The third line will display the minimum time.

##Then run the unit tests by typing

##pytest test_analyze_water.py

##into the command line.


