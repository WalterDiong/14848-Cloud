How to run the datatool box:

Pulling docker images:
1. Pull the following images from dockerhub
(a) docker pull jupyter/base-notebook (jupyter)
(b) docker pull sonarqube (sonarqube and sonarscanner)
(c) docker pull bitnami/spark (spark)
(d) docker pull bde2020/hadoop-namenode:2.0.0-hadoop3.2.1-java8 (hadoop namenode)
(e) docker pull bde2020/hadoop-datanode:2.0.0-hadoop3.2.1-java8(hadoop datanode)
(f) docker pull walterdjs/gui_terminal (terminal/website)

Creating image from terminal application:
1. Run dockerbuild with provided dockerfile and terminal application in the same folder
2. Push the image to dockerhub using "docker push <dockerhubname>/terminal

Retagging images on GCP for container registry:
1. Within the GCP console, pull all the previously pushed images into GCP
2. Retag each of the images running "docker tag <account name>/<image name> gcr.io/<projectid>/walterdjs/<image name>:latest
3. Push the newly tagged image to the container registry using docker push gcr.io/<projectid>/walterdjs/<image name>:latest
3. They will now be in the container registry

Kubernetes step:
1. When creating a new cluster, go to the Kubernetes Engine API and select the create cluster option
2. Select the standard GKE standard option, then select the "My first cluster" option. 
3. When selecting machine congfiguration settings, ensure it is an N1 series machine with the n1-standard-2 option.
4. Also ensure that autoscaling is enabled, with a minimum of 2 nodes selected. 
5. Create the cluster, which will take up to 5 minutes. 

Container deployment on Kubernetes cluster:
1. Go into the folder yaml files and select a yaml file
2. In the Google cloud shell, run the command "kubectl apply -f <yaml file name>" to deploy the pods as intended
3. Repeat for each file in the folder 

Running each service:
1. Once each service has been deployed, go to the IP address of the gui_terminal service
2. You will land on a homepage which will allow you to access the web uis for each of the 4 services
3. Clink of the link that corresponds with the service you wish to access
4. Have fun!

How the toolbox was built:
Constructing the hadoop namenode yaml file:
1. In the Google cloud platform, Google Containter Registry api, select the image you wish to deploy
2. Click on the deploy button, and select deploy to GKE
3. For the Hadoop namenode, ensure that you include the following environment variables:
  (a) CORE_CONF_fs_defaultFS=hdfs://namenode:9000
  (b) CORE_CONF_hadoop_http_staticuser_user=root
  (c) CORE_CONF_hadoop_proxyuser_hue_hosts=*
  (d) CORE_CONF_hadoop_proxyuser_hue_groups=*
  (e) CORE_CONF_io_compression_codecs=org.apache.hadoop.io.compress.SnappyCodec
  (f) HDFS_CONF_dfs_webhdfs_enabled=true
  (g) HDFS_CONF_dfs_permissions_enabled=false
  (h) HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false
  (i) CLUSTER_NAME=<choose a name you want>
4. Select a memorable application name for the namenode application, as we will need it for the data node
5. Once you have deployed, go to the yaml tab and change the value of replicas, to 1 to ensure that
only one namenode is built
6. Expose the namenode of ports 9000 and 9870, and ensure you select the load balancer option

Constructing the datanode yaml file
1. Follow steps 1 to 3 for the namenode yaml file
2. Go to the yaml tab in the data node and change the SERVICE_PRECONDITION value to the name of the namenode
chosen in step 5 of the namenode yaml file construction steps
3. Change the CORE_CONF_fs_defaultFS value to have the name of the namenode chosen in the previous step as well
4. Change the replicas value for this yaml file to 2 as well.

Every other deployment:
1. For every other deployment, you can create as many replicas as you like, and you do not have to worry about 
environment variables. 
2. Ensure that jupyter is exposed on port 8888, spark is exposed on port 8080, sonarqubescanner on port 9000, 
the namenode on port 9870, and the gui_terminal on port 80



