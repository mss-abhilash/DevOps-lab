\# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets



\## Objective

Deploy two Flask applications on a three-node Minikube cluster using Kubernetes Deployments, replicas, Services, and pod anti-affinity to improve availability and distribute workloads across nodes.



\## Applications



\### 1. Product Catalog

\- File: `product\_catalog.py`

\- Endpoint: `GET /products`

\- Returns a JSON list of three products: Laptop, Phone, and Headphones.

\- Replicas: 2



\### 2. Shopping Cart

\- File: `shopping\_cart.py`

\- Endpoints:

&#x20; - `GET /cart` — View cart items.

&#x20; - `POST /cart` — Add an item to the cart.

\- Replicas: 3



\## Technologies Used

\- Python and Flask

\- Docker

\- Kubernetes

\- Minikube

\- PowerShell

\- Git and GitHub



\## Project Structure



```text

10-Multi-Node-Kubernetes/

├── Images/

├── product\_catalog.py

├── shopping\_cart.py

├── Dockerfile.product

├── Dockerfile.shopping

├── product\_catalog\_deployment.yaml

├── shopping\_cart\_deployment.yaml

├── product\_catalog\_service.yaml

├── shopping\_cart\_service.yaml

└── README.md

```



\## Kubernetes Configuration

\- Minikube profile: `devops-multinode`

\- Cluster nodes: 3

\- Product Catalog replicas: 2

\- Shopping Cart replicas: 3

\- Both applications use `NodePort` Services.

\- Pod anti-affinity is configured to keep replicas of each application on separate nodes.



\## Implementation Steps

1\. Created the three-node Minikube cluster.

2\. Enabled the Minikube registry addon.

3\. Created the two Flask applications.

4\. Built Docker images for both applications.

5\. Loaded the images into the Minikube cluster.

6\. Created and applied Kubernetes Deployments and Services.

7\. Verified that all five Pods were running across the three nodes.

8\. Tested the Product Catalog and Shopping Cart endpoints.



\## Testing



\### Product Catalog

Endpoint: `GET /products`



Expected response:



```json

\[

&#x20; {"id": 1, "name": "Laptop", "price": 1200},

&#x20; {"id": 2, "name": "Phone", "price": 800},

&#x20; {"id": 3, "name": "Headphones", "price": 150}

]

```



\### Shopping Cart

\- `GET /cart` initially returned an empty list: `\[]`.

\- `POST /cart` successfully added a laptop.

\- A subsequent `GET /cart` confirmed that the laptop was present with quantity 1.



\## Screenshots

Screenshots demonstrating the implementation and testing are stored in the `Images/` folder.



\- `10-pods-distribution.png` — Pod status and node distribution.

\- `10-shopping-cart-test.png` — Shopping Cart endpoint testing.



\## Result

Successfully deployed two Flask applications on a three-node Minikube cluster with five replicas in total. Verified that all Pods were running across the cluster and that the Shopping Cart API could add and retrieve items.



\*\*Note:\*\* The Shopping Cart stores data in memory, so items may be lost if the container restarts.



