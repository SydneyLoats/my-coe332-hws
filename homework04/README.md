Once Upon a Time in Containers
==============================
This homework is an introduction to containers where we used Docker to containerize code that analyzes Meteorite Landings data. This homework had us use a file called ml_data_analysis.py to read in data from Meteorite_Landings.json and output summarized information from the json file. A file called `test_ml_data_analysis.py` was then created with unit tests to test three functions from `ml_data_analysis.py`, `compute_average_mass()`, `check_hempishpere()`, and `count_classes()`.

Files
-------
1. `Dockerfile` is the file that containerizes the `ml_data_analysis.py` script.

2. `ml_data_analysis.py` is the python3 file that was altered so that it summarizes the Meteorite Landing data from a file entered through the command line.

3. `test_ml_data_analysis.py` is the python3 file that houses the unit tests for `ml_data_analysis.py`.

4. `Meteorite_Landings.json` is the json file that contains Meteorite Landing data.

How to Run the Code
-------------------
1. Build the docker file using the following command: `docker build -t username/ml_data_analysis:1.0 -f Dockerfile`

2. Run the docker file using the following command: `docker run --rm -v $PWD:/data username/ml_data_analysis:1.0 ml_data_analysis.py /data/ml.json`
