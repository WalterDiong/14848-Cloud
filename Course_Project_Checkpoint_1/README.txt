Notes:
Terminal expects console input to select which service to run. As no input is provided into terminal application, container reflects as 
failed. You will see that all pods are up and running on the cluster for the terminal application.
Otherwise, it is successfully deployed to kuberenetes cluster along with all other containers. 

Pulling docker images:
Pull the following images from dockerhub:
(a) docker pull jupyter/base-notebook (jupyter)
(b) docker pull sonarqube (sonarqube and sonarscanner)
(c) docker pull bitnami/spark (spark)
(d) docker pull ibmcom/iop-hadoop (hadoop)

Creating image from terminal application:
1. Run dockerbuild with provided dockerfile and terminal application in the same folder
2. Push the image to dockerhub using "docker push <dockerhubname>/terminal

Retagging images on GCP for container registry:
1. Within the GCP console, pull all the previously pushed images into GCP
2. Retag each of the images running "docker tag walterdjs/<image name> gcr.io/<projectid>/walterdjs/<image name>:latest
3. Push the newly tagged image to the container registry using docker push gcr.io/<projectid>/walterdjs/<image name>:latest
3. They will now be in the container registry

Kubernetes step:
1. When creating a new cluster, go to the Kubernetes Engine API and select the create cluster option
2. Select the standard GKE standard option, then select the "My first cluster" option. 
3. When selecting machine congfiguration settings, ensure it is an N1 series machine with the n1-standard-2 option.
4. Also ensure that autoscaling is enabled, with a minimum of 2 nodes selected. 
5. Create the cluster, which will take up to 5 minutes. 

Container deployment on Kubernetes cluster:
1. Go into the google container registry on GCP and go into the folder where all the images are located
2. Select the image you wish to deploy to the recently created Kubernetes cluster and click the deploy option
3. Click the deploy to GKE option, rename the application, and ensure that the kubernetes cluster is selected.
4. Deploy the cluster and wait for the container to get deployed. 
5. Repeat for each image you wish to deploy to the cluster. 

Port mapping and exposition:
1. (a)For Jupyter, click the expose option and ensure the port and target port are set to 8888.
   (b)Inspect the YAML file to ensure the port and target ports have been modified.
2. (a)For SonarQube & Scanner, click the expose option and ensure the port and target port are set to 9000.
   (b)Inspect the YAML file to ensure the port and target ports have been modified.
3. (a)For SonarQube & Scanner, click the expose option and ensure the port and target port are set to 9000.
   (b)Inspect the YAML file to ensure the port and target ports have been modified.