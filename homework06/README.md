Deploying Our Flask API to Kubernetes
=====================================
The purpose of this homework is to use Kubernetes(k8s) to deploy our flask API to retrieve information about meteorite landings from the file 'ML_Data_Sample.json'. This homework builds off of the Flask application we created in the previous homework. Once we ssh into Kubernetes and follow the necessary steps toapply each file into Kubernetes, we will be able to use the same curl methods as in the last homework to load in meteorite landing data from a json file and outputs the data in a way that is easy for the user to view.

Download Positional and Sighting Data
-------------------------------------
1. Navigate to `https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json` if you would like to see the data in a browser.

2. Login to the TACC computer, create a new directory, and download the positional data by typing `wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json` into the terminal.

SSH to Kubernetes
-----------------
1. Ensure that you are logged into the TACC isp02 computer and type the following line to SSH to Kubernetes.

`ssh <tacc username>@coe332-k8s.tacc.cloud`

Apply Each File in Kubernetes
-----------------------------
1. Apply each of the yml files by typeing the following line into the command line for each yml file.

`kubectl apply -f <filename>`

Exec into the Running Pod for Deployment
----------------------------------------
1. Type `kubecl get pods` into the command line to see all of the files you just applied.

2. You will now be able to identify the pod name. It should look similar to the following:

`hello-pvc-deployment-74f98fffb-g9zd7`

3. This pod name can now be used to exec into the running pod. Type the following into the command line.

`kubectl exec -it <pod_name> -- /bin/bash`

Running the Application using Curl
----------------------------------
1. Now that we are in the running pod, we can use the usual curl methods to run the flask application.

2. Type `curl <flask port>/data -X POST` to load the meteorite landing data. You will recieve a message "Data loaded from file to dictionary." when the data is loaded.

3. Type `curl <flask port>/data` to return a json string of the meteorite landing data. The data should look like the following:

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


Each meteorite landing has a unique name, like Gerald and Dominique, and includes information about its id, recclass, mass in grams, reclat, reclong, and GeoLocation coordinates.
 
