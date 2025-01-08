Helm chart will have the following structure:
flask-mysql-app/  
  ├── Chart.yaml  
  ├── values.yaml  
  ├── templates/  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── flask-deployment.yaml  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── flask-service.yaml  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── mysql-statefulset.yaml  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── mysql-service.yaml  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── configmap.yaml  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── secret.yaml  


Note: _Content of the files mentioned below are in the project root directpry_  


Step 1: Create Chart.yaml  
Step 2: Create values.yaml  
    &nbsp;&nbsp;Replace the placeholder passwords with your actual passwords in this file.  
Step 3: Create ConfigMap and Secret  
Step 4: Create MySQL StatefulSet and Service  
Step 5: Create Flask Deployment and Service  
Step 6: Install the Helm Chart  

**Verify the Deployment**    
1. List the Pods:  
    &nbsp;&nbsp;kubectl get pods  
2. Get Services:  
    &nbsp;&nbsp;kubectl get svc  
3. Access the Flask Application:  
    &nbsp;&nbsp;Forward the port to your local machine: **kubectl port-forward svc/my-release-flask 8080:8080**  
    &nbsp;&nbsp;Open your web browser and navigate to http://localhost:8080/.

