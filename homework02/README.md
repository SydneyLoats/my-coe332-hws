Investigating Meteorite Sites
=============================
This homework generates random data and stores it in a json file. This data is then used to calulate distances and times that it takes for a robot vehicle to collect soil samples on mars. 

Files
-----
1. `generate_sites.py` generates random data and stores it in a json file called sites.json. The data contains information about 5 meteorite landing sites: site id number, latitude, longitude, and composition of the soil at the site (either stony, iron, or stony-iron).

2. `calculate_trip.py` uses the information from sites.json to calculate the time it takes to travel between the 5 sites and time to sample the soil This file outputs time to travel and time to sample at each of the five legs of the trip.

Run the Code
------------
1. Generate the `sites.json` file by typing `python3 generate_sites.py` into the command line.

2. Calculate the distances and times to complete the trop by typing `python3 calculate_trip.py` into the command line. This will produce output data for each leg and the trip as a whole.
