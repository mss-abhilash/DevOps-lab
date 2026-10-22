\# Exercise 2: Deploy a Flask Application on Kubernetes



\## Objective

Deploy a Python Flask web application on Kubernetes using Docker and Minikube. Build a Docker image, deploy it using a Kubernetes Deployment, expose it through a NodePort Service, and verify that the application is accessible.



\## Technologies Used

\- Python

\- Flask

\- Docker

\- Kubernetes

\- Minikube

\- PowerShell



\## Project Structure



```text

2-Flask-Kubernetes/

├── app.py

├── Dockerfile

├── flask-deployment.yaml

├── flask-service.yaml

├── README.md

└── Images/

```



\## Application Details



The Flask application runs on port `15000` and exposes a route at `/`.



When accessed successfully, it returns:



`Hello from Flask on Kubernetes!`



\## Implementation Steps



\### 1. Build the Docker Image



Configure Docker to use Minikube's Docker environment and build the image:



```powershell

minikube docker-env --shell powershell | Invoke-Expression

docker build -t flask-app .

```



\### 2. Deploy the Application



Apply the Kubernetes Deployment configuration:



```powershell

kubectl apply -f flask-deployment.yaml

```



\### 3. Verify the Deployment



Check the Deployment and Pods:



```powershell

kubectl get deployments

kubectl get pods -l app=flask-app

```



\### 4. Expose the Application



Apply the Service configuration:



```powershell

kubectl apply -f flask-service.yaml

```



\### 5. Access and Test the Application



Retrieve the service URL:



```powershell

minikube service flask-app-service --url

```



Use the URL returned by Minikube to test the application:



```powershell

curl.exe http://127.0.0.1:<PORT>

```



Replace `<PORT>` with the port in the returned URL.



Expected response:



```text

Hello from Flask on Kubernetes!

```



\## Verification



The exercise is successful when:

\- The Docker image builds successfully.

\- The Flask Deployment is available.

\- The Pod is running.

\- The NodePort Service is created.

\- The application returns the expected response.



\## Screenshots



The `Images/` folder contains screenshots demonstrating the Docker image build, Kubernetes Deployment and Pod status, Service configuration, and successful application response.



\## Result



Successfully containerized a Flask application using Docker, deployed it to Kubernetes through Minikube, exposed it using a NodePort Service, and verified its HTTP response.



