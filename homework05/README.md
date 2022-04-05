Back to the Flask- Using Redis for Meteorite Landing Data
=========================================================
The purpose of this homework is to use Docker to containerize a Flask application and a Redis database server to retrieve information about meteorite landings from the file 'ML_Data_Sample.json'. The file app.py loads in meteorite landing data from a json file and outputs the data in a way that is easy for the user to view.

Download Positional and Sighting Data
-------------------------------------
1. Navigate to `https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json` if you would like to see the data in a browser.

2. Login to the TACC computer, create a new directory, and download the positional data by typing `wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json` into the terminal.

Launching a Redis Database Server
---------------------------------
1. Launch a Redis database server by typing `docker run -d -p 6379:6379 -v $(pwd)/data:/data:rw --name=<name> redis:6 --save 1 1` into the terminal.

Creating a Dockerfile
---------------------
1. If the Dockerfile is not already created, create a Dockerfile with the following text:
`
	FROM python:3.9  

	RUN mkdir /app  
	RUN pip3 install --user redis  
	WORKDIR /app  
	COPY requirements.txt /app/requirements.txt  
	RUN pip install -r /app/requirements.txt  
	COPY . /app  
`

ENTRYPOINT ["python"]
CMD ["app.py"]

Build the Flask Application
---------------------------
1. Ensure the Dockerfile file and the app.py files are in the same directory as the ML_Data_Sample.json file.

2. Type `export FLASK_APP=app.py` into the terminal.

3. Type `export FLASK_ENV=development` into the terminal.

4. Type `flask run -p <flask port>` into the terminal.

Instructions to Interact With All Routes Using curl
---------------------------------------------------
1. Log onto the TACC computer on a second terminal.

2. Type `curl localhost:<flask port>/data -X POST` to load the meteorite landing data. You will recieve a message "Data loaded from file to dictionary." when the data is loaded.

3. Type `curl localhost:<flask port>/data` to return a json string of the meteorite landing data. The data should look like the following:

{  
  "meteorite_landings": [  
    {  
      "name": "Gerald",  
      "id": "10001",  
      "recclass": "H4",  
      "mass (g)": "5754",  
      "reclat": "-75.6691",  
      "reclong": "60.6936",  
      "GeoLocation": "(-75.6691, 60.6936)"  
    },  
    {  
      "name": "Dominique",  
      "id": "10002",  
      "recclass": "L6",  
      "mass (g)": "1701",  
      "reclat": "-9.4378",  
      "reclong": "49.5751",  
      "GeoLocation": "(-9.4378, 49.5751)"  
    },  



