# Flask GIF App

## Overview
This is a Flask-based web application that fetches random Ryan Gosling GIFs from the web and displays them. The application is deployed using **Kubernetes** with **Helm**, and the infrastructure is managed with **Terraform**. The backend database used is **MySQL**.

## Features
- Fetches and displays random GIFs
- Stores GIF URLs in a MySQL database
- Deployed using **Helm** and **Kubernetes**
- Infrastructure managed using **Terraform**
- CI/CD pipeline for automated deployments

## Technologies Used
- **Flask** (Python web framework)
- **MySQL** (Relational Database)
- **Kubernetes** (Container orchestration)
- **Helm** (Kubernetes package manager)
- **Terraform** (Infrastructure as Code)
- **GitHub Actions / GitLab CI** (CI/CD automation)

## Prerequisites
Before running the project, ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Kubernetes (kubectl)](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) (if deploying on GCP)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/amitayalmog/flask-app.git
cd flask-gif-app
```

### 2. Build and Push Docker Image
```bash
docker build -t gcr.io/YOUR_PROJECT_ID/flask-app:latest .
docker push gcr.io/YOUR_PROJECT_ID/flask-app:latest
```

### 3. Deploy Database
```bash
kubectl apply -f kubernetes/mysql-deployment.yaml
```

### 4. Deploy the Application with Helm
```bash
helm repo add flask-app https://amitayalmog.github.io/helm-flaskgif
helm install flask-app flask-app/
```

### 5. Check Deployment Status
```bash
kubectl get pods
kubectl get services
```

### 6. Access the Application
Find the external IP of the LoadBalancer service:
```bash
kubectl get svc flask-app-service
```
Open the IP in your browser:
```
http://EXTERNAL_IP:8080
```

## Terraform Deployment
If using Terraform for infrastructure setup:
```bash
terraform init
terraform apply -auto-approve
```

## Troubleshooting
### **ImagePullBackOff Error**
- Ensure the Docker image is pushed to the correct registry.
- Run `kubectl describe pod <pod-name>` for more details.
- Check if Kubernetes can access the image with `kubectl get pods -o wide`.

### **State Lock Issue in Terraform**
If you encounter an error like:
```
Error acquiring the state lock
```
Run the following command to force unlock:
```bash
terraform force-unlock -force <LOCK_ID>
```

## Contributing

Feel free to submit pull requests or report issues!

## License
MIT License


![Untitled Diagram](https://github.com/user-attachments/assets/32e8f3d0-cdb1-4419-914c-b67cabf51ade)
