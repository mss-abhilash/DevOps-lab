\# Exercise 5: Docker Security with AppArmor and Python



\## Objective



To understand how to secure Docker containers using AppArmor profiles and Python. This exercise demonstrates how to create an AppArmor profile, apply it to a Docker container, and test restricted actions using the Docker SDK for Python.



\## Technologies Used



\- Docker

\- Docker AppArmor security profiles

\- Python

\- Flask

\- Docker SDK for Python

\- Linux



\## Prerequisites



\- Docker installed and running

\- Python installed

\- A Linux environment with AppArmor support

\- `apparmor-utils` installed

\- Docker SDK for Python installed



Install AppArmor utilities on Ubuntu/Debian:



```bash

sudo apt-get update

sudo apt-get install apparmor-utils

```



Install the Docker SDK for Python:



```bash

pip install docker

```



\## Task 1: Create the Flask Application



Create a file named `app.py`:



```python

from flask import Flask



app = Flask(\_\_name\_\_)



@app.route('/')

def home():

&#x20;   return "Hello, this is a secure Flask application running inside a Docker container!"



if \_\_name\_\_ == '\_\_main\_\_':

&#x20;   app.run(host='0.0.0.0', port=5000)

```



The application provides a simple HTTP endpoint on port `5000`.



\## Task 2: Containerize the Application



Create a file named `Dockerfile`:



```dockerfile

FROM python:3.8-slim



WORKDIR /app



COPY . /app



RUN pip install flask



EXPOSE 5000



CMD \["python", "app.py"]

```



Build the Docker image:



```bash

docker build -t flask-apparmor .

```



The image is named `flask-apparmor`.



\## Task 3: Create and Apply an AppArmor Profile



Create the profile file at:



`/etc/apparmor.d/my-apparmor-profile`



Profile configuration:



```text

\#include <tunables/global>



/usr/bin/python3 {

&#x20;   deny /etc/\*\* r,

&#x20;   deny /var/\*\* rw,



&#x20;   network inet stream,



&#x20;   /app/\*\* rwk,



&#x20;   deny /bin/\*\* rmix,

&#x20;   deny /usr/bin/\*\* rmix,



&#x20;   capability net\_bind\_service,

&#x20;   deny capability sys\_admin,

}

```



Load or reload the profile:



```bash

sudo apparmor\_parser -r /etc/apparmor.d/my-apparmor-profile

```



Run the container with the profile:



```bash

docker run -d --name flask-secure \\

&#x20; --security-opt="apparmor=my-apparmor-profile" \\

&#x20; -p 5000:5000 flask-apparmor

```



The `--security-opt` option specifies the AppArmor profile to apply to the container.



\## Task 4: Apply AppArmor Using the Docker SDK for Python



Create `apply\_apparmor.py`:



```python

import docker



client = docker.from\_env()



client.images.build(path=".", tag="flask-apparmor")



container = client.containers.run(

&#x20;   "flask-apparmor",

&#x20;   ports={'5000/tcp': 5000},

&#x20;   security\_opt=\["apparmor=my-apparmor-profile"],

&#x20;   detach=True

)



print(f"Container started: {container.short\_id}")



container\_info = client.api.inspect\_container(container.id)

apparmor\_profile = container\_info\['HostConfig']\['SecurityOpt']



print(f"AppArmor profile applied: {apparmor\_profile}")



container.stop()

container.remove()

```



Run the script:



```bash

python apply\_apparmor.py

```



The script builds the image, starts a container with the specified AppArmor profile, inspects the container's security options, and then stops and removes the container.



\## Task 5: Test Restricted Actions



Create `test\_restricted\_actions.py`:



```python

import docker



client = docker.from\_env()



container = client.containers.run(

&#x20;   "flask-apparmor",

&#x20;   ports={'5000/tcp': 5000},

&#x20;   security\_opt=\["apparmor=my-apparmor-profile"],

&#x20;   detach=True

)



print(f"Container started: {container.short\_id}")



exit\_code, output = container.exec\_run("cat /etc/passwd")

print(

&#x20;   f"Attempt to read /etc/passwd: "

&#x20;   f"Exit Code {exit\_code}, Output: {output.decode()}"

)



exit\_code, output = container.exec\_run("/bin/bash")

print(

&#x20;   f"Attempt to execute /bin/bash: "

&#x20;   f"Exit Code {exit\_code}, Output: {output.decode()}"

)



container.stop()

container.remove()



print("Container stopped")

```



Run the script:



```bash

python test\_restricted\_actions.py

```



The script attempts to read `/etc/passwd` and execute `/bin/bash` inside the container. The expected result is that restricted actions fail under the configured profile.



Actual results depend on the AppArmor profile, container image, and host environment.



\## Questions and Answers



\### 1. What is the purpose of using AppArmor with Docker containers?



AppArmor enforces security policies that confine applications to a limited set of resources. With Docker, it adds a layer of security by restricting access to files, system resources, and network operations.



\### 2. How do AppArmor profiles help secure a Docker container?



AppArmor profiles specify which operations an application can perform. They can restrict file access, binary execution, network operations, and capabilities to reduce the risk of unauthorized actions.



\### 3. Why is it important to restrict access to sensitive directories such as `/etc/` and `/var/`?



The `/etc/` directory contains system configuration files, while `/var/` can contain logs, application data, and other changing system files. Restricting access helps prevent unauthorized reading or modification of sensitive information.



\### 4. What other capabilities can you restrict using AppArmor profiles?



AppArmor can restrict file and directory access, execution of programs, network operations, and certain system capabilities. For example, a profile can deny the `sys\_admin` capability to reduce the application's ability to perform privileged system operations.



\### 5. How can you verify if an AppArmor profile is successfully applied to a Docker container?



Inspect the container's security configuration using the Docker CLI or Docker SDK for Python.



```bash

docker inspect flask-secure

```



In the output, examine `HostConfig.SecurityOpt` for the configured AppArmor option. On a Linux host, AppArmor status and process confinement can also be checked using AppArmor utilities.



\## Result



A Flask application was containerized using Docker, and an AppArmor profile was configured to restrict selected operations. The Docker SDK for Python was used to launch a container with the profile and inspect its security options. Restricted actions were tested to evaluate the effect of the profile.



\## Conclusion



This exercise demonstrates how AppArmor profiles can provide an additional security layer for Docker containers. It also illustrates how Python's Docker SDK can automate container creation, profile configuration, inspection, and testing of restricted operations.



