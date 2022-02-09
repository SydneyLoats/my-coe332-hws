
Sydney Loats SML4267 homework02 README file

homework02 creates a json file with data and uses that data to calulate distances and times that it takes for a robot vehicle to collect soil samples on mars
This folder holds two additional files,
    generate_sites.py
    calculate_trip.py

The file generate_sites.py creates a json file called sites.json that holds information about 5 meteorite landing sites,
such as 
    site id number
    latitude
    longitude
    composition of the soil at the site (either stony, iron, or stony-iron)


The file calculate_trip.py uses the information from sites.json to calculate the time it takes to travel between the 5 sites and time to sample the soil
This file outputs time to travel and time to sample at each of the five legs of the trip
This file also outputs 



To run this code, 

first generate the sites.json file as follows
     
   python3 generate_sites.py

then calculate the distances and times it takes to complete the trip

   python3 calculate_trip.py

now the code should have output the data for each leg and the trip as a whole

     
