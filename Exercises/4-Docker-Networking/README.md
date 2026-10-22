\# Exercise 4: Docker Networking with Multiple Containers



\## Objective



Understand Docker networking concepts and configure a multi-container application using a custom bridge network.



\## Scenario



The exercise uses three containers:



\- \*\*Flask:\*\* Python web application providing a REST API.

\- \*\*MySQL:\*\* Database container.

\- \*\*Redis:\*\* Cache container.



All three containers are connected to the same custom Docker bridge network to enable container-to-container communication.



\## Technologies Used



\- Docker

\- Docker Bridge Networking

\- Python

\- Flask

\- MySQL

\- Redis



\## Implementation



\### Task 1: Create a Bridge Network



Create a custom bridge network named `my-bridge-net`.



```bash

docker network create --driver bridge my-bridge-net

```



\### Task 2: Verify the Network



List the Docker networks and verify that the custom network exists.



```bash

docker network ls

```



Expected result: `my-bridge-net` appears in the list with the `bridge` driver.



\### Task 3: Inspect the Network



Inspect the network configuration.



```bash

docker network inspect my-bridge-net

```



The output provides information about the network driver, subnet, gateway, and connected containers. The subnet and gateway depend on the Docker environment.



\### Task 4: Create the Flask Application



Create `app.py`:



```python

from flask import Flask, jsonify



app = Flask(\_\_name\_\_)



@app.route('/about', methods=\['GET'])

def about():

&#x20;   return jsonify({

&#x20;       "name": "Simple REST API",

&#x20;       "version": "1.0",

&#x20;       "description": "This is a simple REST API built with Flask."

&#x20;   })



if \_\_name\_\_ == '\_\_main\_\_':

&#x20;   app.run(host='0.0.0.0', debug=True, port=5001)

```



The application provides a GET endpoint at `/about`. Binding to `0.0.0.0` allows the application to accept connections through the container's network interface.



Create `requirements.txt`:



```text

Flask==2.0.1

```



Create the `Dockerfile`:



```dockerfile

FROM python:3.9-slim



WORKDIR /app



COPY requirements.txt .

COPY app.py .



RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 5001



CMD \["python", "app.py"]

```



\### Task 5: Build the Flask Image



Build the Docker image.



```bash

docker build -t flask-api .

```



\### Task 6: Launch the Containers



Start the MySQL container:



```bash

docker run -d --name mysql --net=my-bridge-net mysql:latest

```



Start the Redis container:



```bash

docker run -d --name redis --net=my-bridge-net redis:latest

```



Start the Flask container and publish port 5001:



```bash

docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api

```



The `-d` flag runs containers in detached mode. The `--net` flag connects each container to the custom bridge network, while `-p` publishes the Flask port to the host.



\*\*Note:\*\* MySQL may require a root password or other initialization settings, depending on the image configuration. Configure these if needed for your environment.



\### Task 7: Verify Container Status



Check the running containers:



```bash

docker ps

```



All three containers should appear if they started successfully.



\### Task 8: Test the Flask API



Open the endpoint in a browser or run:



```bash

curl.exe http://localhost:5001/about

```



Expected JSON response:



```json

{

&#x20; "name": "Simple REST API",

&#x20; "version": "1.0",

&#x20; "description": "This is a simple REST API built with Flask."

}

```



\### Task 9: Test Container Connectivity



Open a shell in the Flask container:



```bash

docker exec -it flask sh

```



Test name resolution and connectivity to MySQL and Redis:



```bash

ping mysql

ping redis

```



If `ping` is not installed in the Flask image, use an available networking diagnostic tool or test name resolution with Python. Successful communication depends on all containers being connected to `my-bridge-net` and the relevant services being available.



Exit the container shell:



```bash

exit

```



\### Task 10: Clean Up



Stop the containers:



```bash

docker stop mysql redis flask

```



Remove the containers:



```bash

docker rm mysql redis flask

```



Remove the custom bridge network:



```bash

docker network rm my-bridge-net

```



\## Questions and Answers



\### 1. What is the purpose of the `--net` flag in `docker run`?



The `--net` flag specifies the Docker network to which a container should connect. In this exercise, it connects the Flask, MySQL, and Redis containers to `my-bridge-net`.



\### 2. How do containers communicate with each other on the same network?



Containers on the same user-defined bridge network can communicate using their container names or IP addresses. Container names are generally easier to use because Docker provides name resolution on user-defined bridge networks.



\### 3. What is the difference between a bridge network and a host network?



\- \*\*Bridge network:\*\* Containers use an isolated virtual network and communicate through that network. Ports can be published to the host using `-p`.

\- \*\*Host network:\*\* The container shares the host's network namespace rather than using an isolated bridge network. Port publishing is generally unnecessary and ignored in host-network mode.



\### 4. How can you expose a container's port to the host machine?



Use the `-p` option with `docker run`. For example:



```bash

docker run -d --name flask --net=my-bridge-net -p 5001:5001 flask-api

```



This maps port 5001 on the host to port 5001 in the container.



\## Result



A custom Docker bridge network named `my-bridge-net` was created and inspected. Flask, MySQL, and Redis containers were configured to use the same network. The Flask application exposes a REST API on port 5001, and container connectivity can be tested using container names.



\## Conclusion



This exercise demonstrates how to create and inspect a custom Docker bridge network, connect multiple containers, publish a container port to the host, test container communication, and clean up the resources after testing.



