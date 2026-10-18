\# Exercise 9: Jenkins Multi-Stage Pipeline for a Python Flask Application



\## 1. Objective



To implement a Jenkins CI/CD pipeline for a Python Flask application using multiple stages: Build, Test, Deploy, and Test Application. The exercise demonstrates automated dependency installation, unit testing, and deployment to a mock directory.



\## 2. Tools and Technologies



\- Jenkins 2.580.1

\- Docker

\- Python 3.13

\- Flask 2.1.2

\- Werkzeug 2.1.2

\- Git and GitHub

\- Python `unittest` framework

\- Jenkins Declarative Pipeline



\## 3. Project Structure



```text

9-Jenkins-Multi-Stage-Pipeline/

├── Images/

├── Jenkinsfile

├── README.md

└── python-flask-app/

&#x20;   ├── app.py

&#x20;   ├── requirements.txt

&#x20;   └── test\_app.py

```



\## 4. Python Flask Application



The application is defined in `python-flask-app/app.py`.



```python

from flask import Flask



app = Flask(\_\_name\_\_)



@app.route("/")

def home():

&#x20;   return "Hello, Jenkins Multi-Stage Pipeline!"



if \_\_name\_\_ == "\_\_main\_\_":

&#x20;   app.run(debug=True)

```



When the home route (`/`) is requested, the application returns:



`Hello, Jenkins Multi-Stage Pipeline!`



\## 5. Dependencies



The dependencies are specified in `python-flask-app/requirements.txt`.



```text

flask==2.1.2

Werkzeug==2.1.2

```



Werkzeug is pinned to version 2.1.2 to maintain compatibility with Flask 2.1.2.



The Jenkins pipeline creates a Python virtual environment and installs the dependencies into it.



\## 6. Unit Testing



The file `python-flask-app/test\_app.py` contains a unit test that uses Flask's test client to check the home route.



The test verifies that:



\- The HTTP response status code is 200.

\- The response body is `Hello, Jenkins Multi-Stage Pipeline!`



The test is executed using Python's `unittest` framework.



\## 7. Jenkins Pipeline Configuration



A Jenkins Pipeline job named `Python-MultiStage-Pipeline` was created.



The job uses the following configuration:



\- \*\*Repository:\*\* `https://github.com/mss-abhilash/DevOps-lab.git`

\- \*\*Branch:\*\* `main`

\- \*\*Pipeline definition:\*\* Pipeline script from SCM

\- \*\*SCM:\*\* Git

\- \*\*Script path:\*\* `Exercises/9-Jenkins-Multi-Stage-Pipeline/Jenkinsfile`



\## 8. Pipeline Stages



\### Stage 1: Build



\- Creates a Python virtual environment.

\- Upgrades pip within the virtual environment.

\- Installs Flask and its dependencies from `requirements.txt`.



\### Stage 2: Test



\- Runs the Python unit tests using `unittest`.

\- Verifies the home route's response status and content.



\### Stage 3: Deploy



\- Creates a mock deployment directory named `python-app-deploy` inside the Jenkins workspace.

\- Copies `app.py`, `requirements.txt`, and `test\_app.py` into the directory.



\### Stage 4: Test Application



\- Executes the unit tests against the deployed application files.

\- Verifies that the application can be imported and its home route works correctly.



\## 9. Execution and Results



The pipeline was executed from Jenkins using \*\*Build Now\*\*.



During implementation, the pipeline was updated to:



\- Use a Python virtual environment to avoid externally managed Python environment errors.

\- Use the correct application path within the repository.

\- Pin Werkzeug to a compatible version to resolve the Flask import error.



After these corrections, the pipeline completed successfully.



Expected final status:



```text

Pipeline completed successfully!

Finished: SUCCESS

```



\## 10. Screenshots



The `Images` directory is intended to contain screenshots of:



\- The project folder structure.

\- The Jenkins Pipeline configuration.

\- The pipeline stages and their execution.

\- The Console Output showing successful unit tests and pipeline completion.



\## 11. Conclusion



Successfully implemented and executed a Jenkins multi-stage pipeline for a Python Flask application. The pipeline automates dependency installation, unit testing, copying application files to a mock deployment directory, and testing the deployed files.



The exercise demonstrates the use of Jenkins Declarative Pipelines to automate essential CI/CD workflow stages.



\## 12. GitHub Repository



Repository: https://github.com/mss-abhilash/DevOps-lab



Exercise directory: `Exercises/9-Jenkins-Multi-Stage-Pipeline/`



