[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## MLOps Sample Project 🚀
Welcome to this fantastic MLOps Sample Project! 😄 We will guide you through an end-to-end machine learning pipeline, from data preprocessing to model deployment, using MLOps best practices. Get ready to build a regression model that predicts housing prices using the classic Boston Housing dataset. 🏠

## Table of Contents 📚
Project Structure
Installation
Clone Repository
Create a Virtual Environment
Install Dependencies
Usage
Train the Model
Run the Flask App
Deploy to Production
Docker Deployment
Kubernetes Deployment
AWS Deployment
Contributing

## Project Structure 🏗️

[!Directory]("directory.png")

This project structure includes the Flask app, data, model training script, Dockerfile for containerization, Kubernetes configuration files for deployment, and a README file with detailed instructions on how to use the project.


## Installation 💻
Clone Repository 📥
Clone this repository to your local machine:

```
git clone https://github.com/yourusername/MLOps-Sample-Project.git
cd MLOps-Sample-Project
```

## Create a Virtual Environment 🌐
Create a Python virtual environment to manage dependencies:

```
python3 -m venv venv
source venv/bin/activate
```
Install Dependencies 📦
Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage 🎮
Train the Model 🚂
Train the regression model on the Boston Housing dataset:

```
python model/train.py
```

This will preprocess the data, train the model, and save the trained model and preprocessing pipeline artifacts to the model/artifacts directory. It will also log relevant metrics and parameters to MLflow.

## Run the Flask App 🌐
Run the Flask app to serve the trained model as an API:

```
python app/main.py
```

The app will be available at http://localhost:5001. Enter feature values in the form, and the app will predict the housing price using the trained model.

## Deploy to Production 🚢
Docker Deployment 🐳
To deploy the app to production using Docker, follow these steps:

Install Docker on your machine.

Build the Docker image:
```
docker build -t mlops-sample-project .
```
Run the docker container
```
docker run -p 5001:5001 mlops-sample-project
```

The app will be available at `http://localhost:5001`.

## Kubernetes Deployment ⚓

To deploy the app using Kubernetes, follow these steps:

[Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) and [minikube](https://minikube.sigs.k8s.io/docs/start/) on your machine.

Start a local Kubernetes cluster:

```bash
minikube start
```

Kubernetes Deployment
To deploy the app to production using Kubernetes, follow these steps:

Push your Docker image to Docker Hub. First, log in to Docker Hub:

```
docker login
```

Then, tag your image:

```
docker tag mlops-sample-project:latest <your-docker-hub-username>/mlops-sample-project:latest
```

Finally, push the image:

```
docker push <your-docker-hub-username>/mlops-sample-project:latest
```

Apply the Kubernetes configuration files to your cluster:
```
kubectl apply -f namespace.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
Check the status of your deployment and service:

```
kubectl -n mlops-sample-project get deployments
kubectl -n mlops-sample-project get services
```

Wait for the deployment to become available and the service to get an external IP address. Once the service has an external IP, you can access the application at http://<external-ip>/.

This setup deploys your application to a Kubernetes cluster and exposes it via a LoadBalancer service. You can further enhance this setup by configuring autoscaling, adding monitoring and logging, and using Kubernetes secrets for managing sensitive data.

AWS Deployment
To deploy the app to AWS, we'll use Amazon Elastic Kubernetes Service (EKS) to manage our Kubernetes cluster and the deployment process.

Prerequisites
Install AWS CLI and configure it with your AWS account credentials.
Install eksctl, the official CLI tool for Amazon EKS, by following the installation instructions.
Install kubectl for interacting with the Kubernetes cluster.
Create an Amazon EKS Cluster
Create a new Amazon EKS cluster using eksctl:

```
eksctl create cluster --name mlops-sample-project --region us-west-2 --managed
```

This command creates a managed Kubernetes cluster in the us-west-2 region. It might take a few minutes for the cluster to be created.

Verify that the cluster has been created and that kubectl is configured to use it:

```
kubectl config use-context mlops-sample-project.us-west-2.eksctl.io
kubectl get nodes
```

Deploy the App
Apply the Kubernetes configuration files to your cluster:

```
kubectl apply -f namespace.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Check the status of your deployment and service:

```
kubectl -n mlops-sample-project get deployments
kubectl -n mlops-sample-project get services
```
Wait for the deployment to become available and the service to get an external IP address. Once the service has an external IP, you can access the application at http://<external-ip>/.

Clean Up
To delete the Amazon EKS cluster and associated resources, run the following command:

```
eksctl delete cluster --name mlops-sample-project --region us-west-2
```
This will remove the EKS cluster and all associated resources, including the deployed application.


## Contributing 🤝
Feel free to contribute by creating issues or submitting pull requests! Let's make this MLOps Sample Project the best it can be! 🎉

Remember to have fun and enjoy the MLOps journey! 🎉 😄



