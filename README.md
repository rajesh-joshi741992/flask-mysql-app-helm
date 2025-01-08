This is a Flask application that connects to a MySQL database and retrieves messages. The application is containerized using Docker

****Prerequisites****

Note: *It is recommended to use an IDE like PyCharm or VSCode for easier project management and development, im using pycharm.*

Before you can run the application, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Python 3.9](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/mysql/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [helm](https://helm.sh/docs/helm/helm_install/)

1. **Setup:**  
-Clone the Repository  
   git clone https://github.com/yourusername/flask-mysql-app.git  
   cd flask-mysql-app
2. **Create a .env File:**  
    &nbsp;&nbsp;Create a .env file in the root directory of the project with the following content:  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MYSQL_SERVER=localhost  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MYSQL_USER=root  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MYSQL_PASSWORD=your_password  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MYSQL_DB=test_db  
Replace your_password with your MySQL root password.  
 
4. **Install Python Dependencies:**  
   &nbsp;&nbsp;Create a requirements.txt file with the following content:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flask==2.0.1  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mysql-connector-python==9.1.0  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python-dotenv==0.19.2  
    &nbsp;&nbsp;Then install the dependencies:  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pip install -r requirements.txt  

******Running the Application Locally******

1. **Ensure MySQL Server is Running**  
    &nbsp;&nbsp;Start your MySQL server. Make sure it is accessible at localhost on port 3306.  
2. **Initialize the Database**  
    &nbsp;&nbsp;Run the SQL script to initialize the database:  
    &nbsp;&nbsp;&nbsp;mysql -u root -p < init.sql  
    &nbsp;&nbsp;Note: _Content of the file init.sql is in the project root directpry_
4. **Run the Flask Application**  
   &nbsp;&nbsp;&nbsp;Activate your virtual environment and then run your flask application  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;venv\Scripts\activate  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python app.py  
   &nbsp;&nbsp;&nbsp;Note: _Content of the file app.py is in the project root directpry_

****Containerizing the Application with Docker****
1. **Create a Dockerfile**  
    &nbsp;&nbsp;Create a **Dockerfile** in the root directory of the project with the necessary instructions to build the Docker image.  
    &nbsp;&nbsp;Note: _Content of the file init.sql is in the project root directpry_
3. **Build the Docker Image**  
    &nbsp;&nbsp;docker build -t helloworldapp .
4. **Run the Docker Container**  
    &nbsp;&nbsp;docker run -p 8080:8080 --env-file .env  --network="host" helloworldapp
5. **Open Browser and try accessing the application using this URL:**  
    &nbsp;&nbsp;http://localhost:8080/

Troubleshooting  
If you encounter any issues, check the container logs for more information:  
&nbsp;&nbsp;&nbsp;docker logs [container_id]

****Create a Helm Chart****

For Helm chart will have the following structure:
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
Step 6: Package the Helm Chart using command: helm package .  
step 7: Install the Helm Chart using command: helm install my-release ./flask-mysql-app-0.1.0.tgz  

**Verify the Deployment**    
1. List the Pods:  
    &nbsp;&nbsp;kubectl get pods  
2. Get Services:  
    &nbsp;&nbsp;kubectl get svc  
3. Access the Flask Application:  
    &nbsp;&nbsp;Forward the port to your local machine: **kubectl port-forward svc/my-release-flask 8080:8080**  
    &nbsp;&nbsp;Open your web browser and navigate to http://localhost:8080/.

