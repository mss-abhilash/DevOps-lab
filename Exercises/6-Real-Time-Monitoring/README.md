\# Exercise 6: Real-Time Operations Monitoring and Alerting



\## Overview



This project implements a real-time monitoring and alerting system for delivery operations using Python, Prometheus, Grafana, and Jenkins. It simulates delivery metrics, collects and monitors them using Prometheus, visualizes them through a Grafana dashboard, and uses Jenkins to execute a monitoring-related pipeline.



\## Objectives



\- Generate real-time delivery metrics using Python.

\- Expose application metrics for Prometheus scraping.

\- Configure Prometheus to collect and evaluate metrics.

\- Define alert rules for pending deliveries and average delivery time.

\- Visualize delivery metrics using Grafana.

\- Create and execute a Jenkins pipeline.



\## Technologies Used



\- \*\*Python\*\* — delivery metrics simulation.

\- \*\*Prometheus\*\* — metrics collection and alert rule evaluation.

\- \*\*Grafana\*\* — monitoring dashboard and visualization.

\- \*\*Jenkins\*\* — pipeline execution.

\- \*\*Docker\*\* — running Prometheus, Grafana, and Jenkins containers.

\- \*\*PromQL\*\* — querying metrics in Prometheus and Grafana.



\## Project Structure



```text

6-Real-Time-Monitoring/

├── delivery\_metrics.py

├── requirements.txt

├── prometheus.yml

├── alert\_rules.yml

├── README.md

└── Images/

&#x20;   ├── 01-python-metrics-running.png

&#x20;   ├── 02-prometheus-metrics-endpoint.png

&#x20;   ├── 03-prometheus-targets-up.png

&#x20;   ├── 04-prometheus-alerts.png

&#x20;   ├── 06-grafana-prometheus-datasource.png

&#x20;   ├── 07-grafana-delivery-dashboard.png

&#x20;   └── 08-jenkins-pipeline-success.png

```



\*The image files listed above are the intended screenshot names. Include only the screenshots actually captured.\*



\## 1. Delivery Metrics Simulation



The Python application uses the `prometheus-client` library to expose metrics on port `8000`.



The application simulates delivery activity and updates the following metrics:



| Metric | Description |

|---|---|

| `total\_deliveries` | Total number of deliveries calculated by the simulator. |

| `pending\_deliveries` | Number of pending deliveries. |

| `on\_the\_way\_deliveries` | Number of deliveries currently on the way. |

| `average\_delivery\_time` | Summary metric recording delivery-time observations in seconds. |



\### Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### Run the simulator



```bash

python delivery\_metrics.py

```



The application exposes metrics at:



`http://localhost:8000/metrics`



Keep the Python application running while testing Prometheus scraping.



\## 2. Prometheus Configuration



Prometheus runs on port `9090` and scrapes the delivery application through the Docker Desktop host address.



The configuration is stored in `prometheus.yml`.



The configured scrape targets are:



\- Prometheus itself: `localhost:9090`

\- Delivery metrics application: `host.docker.internal:8000`



Prometheus targets can be checked at:



`http://localhost:9090/targets`



The `delivery\_service` target should show \*\*UP\*\* when the Python application is accessible.



\## 3. Alert Rules



The alert rules are defined in `alert\_rules.yml`.



\### HighPendingDeliveries



\- \*\*Condition:\*\* `pending\_deliveries > 10`

\- \*\*Duration:\*\* 15 seconds

\- \*\*Severity:\*\* Warning



This rule detects when pending deliveries remain above the configured threshold.



\### HighAverageDeliveryTime



\- \*\*Condition:\*\* `(average\_delivery\_time\_sum / average\_delivery\_time\_count) > 30`

\- \*\*Duration:\*\* 15 seconds

\- \*\*Severity:\*\* Critical



This rule detects when the observed average delivery time exceeds 30 seconds.



The alert status can be viewed at:



`http://localhost:9090/alerts`



\## 4. Grafana Dashboard



Grafana runs on port `3000` and uses Prometheus as its data source.



The dashboard is named \*\*Real-Time Delivery Monitoring\*\* and contains four Stat panels.



| Panel | PromQL query |

|---|---|

| Total Deliveries | `total\_deliveries` |

| Pending Deliveries | `pending\_deliveries` |

| On-the-Way Deliveries | `on\_the\_way\_deliveries` |

| Average Delivery Time | `average\_delivery\_time\_sum / average\_delivery\_time\_count` |



The average delivery time query calculates the mean of the recorded observations in seconds.



Dashboard URL:



`http://localhost:3000`



\## 5. Jenkins Pipeline



A Jenkins job named `Real-Time-Monitoring-Pipeline` was created to execute a pipeline in the Linux-based Jenkins container.



The pipeline includes these stages:



1\. \*\*Check Jenkins Environment\*\* — displays Linux environment information and the current workspace.

2\. \*\*Validate Monitoring Files\*\* — checks whether `prometheus.yml` and `alert\_rules.yml` are present in the Jenkins workspace.

3\. \*\*Pipeline Complete\*\* — prints a successful completion message.



The pipeline uses Linux shell commands through the Jenkins `sh` step.



\*\*Note:\*\* The pipeline validates the Jenkins environment and checks for configuration files in its workspace. It does not automatically deploy or restart Prometheus or Grafana.



\## 6. How to Run the Project



1\. Install Python and Docker Desktop.

2\. Install the Python dependencies.

3\. Start the delivery metrics simulator using `python delivery\_metrics.py`.

4\. Start Prometheus with the provided configuration and alert rules.

5\. Verify the Prometheus targets and alert rules.

6\. Start Grafana and configure Prometheus as the data source.

7\. Create and save the four-panel delivery monitoring dashboard.

8\. Open Jenkins and run the `Real-Time-Monitoring-Pipeline` job.

9\. Capture screenshots of the running application, monitoring targets, alerts, dashboard, and successful Jenkins build.



\## Conclusion



This exercise demonstrates an integrated monitoring workflow for simulated delivery operations. Python generates application metrics, Prometheus scrapes and evaluates those metrics, Grafana visualizes delivery activity, and Jenkins executes a pipeline to check the monitoring project environment and configuration files.

