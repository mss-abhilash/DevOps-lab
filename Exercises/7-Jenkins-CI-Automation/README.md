\# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Installation



\## 1. Objective



To understand the fundamentals of Continuous Integration (CI), install Jenkins using Docker, and create and execute a basic Jenkins job.



\## 2. Tools and Technologies



\- Docker

\- Jenkins LTS

\- Git

\- GitHub

\- PowerShell



\## 3. Jenkins Installation



Jenkins was installed and executed inside a Docker container.



\- \*\*Container name:\*\* `jenkins-ex7`

\- \*\*Jenkins URL:\*\* `http://localhost:8083`

\- \*\*Container port:\*\* `8080`

\- \*\*Host port:\*\* `8083`

\- \*\*Agent communication port:\*\* `50002`



Jenkins initial setup was completed, and an administrator account was created.



\## 4. Jenkins Job Configuration



A Freestyle project named `Exercise-7-CI-Job` was created.



The job was configured with the following build commands:



```sh

echo "Starting Exercise 7 Jenkins CI Job"

echo "Running build checks..."

echo "Build completed successfully!"

```



These commands demonstrate the execution of build steps in a Jenkins job.



\## 5. GitHub Integration



The Jenkins job was configured to use the following public GitHub repository:



https://github.com/mss-abhilash/DevOps-lab.git



The branch specifier was configured as `\*/main`.



Jenkins successfully fetched the repository and checked out the `main` branch.



\## 6. Build Automation



A periodic build trigger was configured using the following schedule:



```text

H/5 \* \* \* \*

```



This schedules builds approximately every five minutes, subject to Jenkins scheduling.



The Jenkins job was executed successfully, and the console output confirmed that the repository checkout and configured build commands completed without errors.



\## 7. Screenshots



The `Images` directory contains screenshots documenting the exercise, including Jenkins configuration and successful build execution.



\## 8. Result



Jenkins was successfully installed using Docker. A Freestyle project was created, connected to a public GitHub repository, and executed successfully. Periodic build scheduling was also configured.



\## 9. Repository



\[DevOps-lab on GitHub](https://github.com/mss-abhilash/DevOps-lab)



