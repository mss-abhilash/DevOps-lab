\# Exercise 8: Creating a Hello World Jenkins Job



\## 1. Objective



To understand the basics of Continuous Integration (CI) by creating a Jenkins Freestyle job that retrieves a shell script from GitHub and executes it.



\## 2. Tools and Technologies



\- Jenkins LTS

\- Docker

\- Git and GitHub

\- Bash shell scripting

\- Windows PowerShell



\## 3. Prerequisites



\- Jenkins running in a Docker container.

\- A public GitHub repository containing the shell script.

\- Git configured locally to commit and push changes.



\## 4. Shell Script



The file `hello-world.sh` contains the following commands:



```bash

\#!/bin/bash

echo "Hello, Jenkins!"

```



The script prints a greeting when executed.



\## 5. GitHub Repository



The project is stored in the following repository:



\[DevOps-lab on GitHub](https://github.com/mss-abhilash/DevOps-lab)



The script is located at:



`Exercises/8-Hello-World-Jenkins-Job/hello-world.sh`



\## 6. Jenkins Job Configuration



A Freestyle project named `HelloWorld-Ex8` was created.



The job was configured with the following settings:



\- \*\*Source Code Management:\*\* Git

\- \*\*Repository URL:\*\* `https://github.com/mss-abhilash/DevOps-lab.git`

\- \*\*Branch:\*\* `\*/main`

\- \*\*Build Step:\*\* Execute shell



The following command was configured as the build step:



```bash

sh Exercises/8-Hello-World-Jenkins-Job/hello-world.sh

```



Jenkins checks out the repository and executes the script from its workspace.



\## 7. Execution and Verification



The Jenkins job was executed using \*\*Build Now\*\*. The Console Output confirmed that the repository was cloned, the `main` branch was checked out, and the shell script ran successfully.



Expected output:



```text

Hello, Jenkins!

Finished: SUCCESS

```



\## 8. Screenshots



The `Images` directory contains screenshots documenting the Jenkins job dashboard, successful build output, and GitHub script, where captured.



\## 9. Result



Successfully created and executed a Jenkins Freestyle job that retrieves a shell script from a GitHub repository and prints `Hello, Jenkins!`. The build completed successfully.



\## 10. Repository Link



\[https://github.com/mss-abhilash/DevOps-lab](https://github.com/mss-abhilash/DevOps-lab)



