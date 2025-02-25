<<<<<<< HEAD
provider "google" {
  project = var.project_id
  region  = var.region
=======
provider "aws" {
  region = "us-east-1" # Change to your preferred region, 6, 25/1 deploy.
<<<<<<< HEAD
>>>>>>> ddb05319b4857cb0125430e0aaf5fac16212995f
}
terraform {
  backend "s3" {
    bucket         = "amitays-bucket"   # Your existing S3 bucket name
    key            = "terraform.tfstate"  # State file location inside the bucket
    region         = "us-east-1"  # Update if your bucket is in a different region
    encrypt        = true
  }
}
resource "aws_security_group" "flask_sg" {
  name        = "flask-sg"
  description = "Security group for Flask app"

<<<<<<< HEAD
terraform {
  backend "gcs" {
    bucket  = "flaski"
    prefix  = "terraform/state"
  }
=======
>>>>>>> ddb05319b4857cb0125430e0aaf5fac16212995f
}
terraform {
  backend "s3" {
    bucket         = "amitays-bucket"   # Your existing S3 bucket name
    key            = "terraform.tfstate"  # State file location inside the bucket
    region         = "us-east-1"  # Update if your bucket is in a different region
    encrypt        = true
  }
}
resource "aws_security_group" "flask_sg" {
  name        = "flask-sg"
  description = "Security group for Flask app"

<<<<<<< HEAD
# Create a GKE cluster
resource "google_container_cluster" "primary" {
  name               = var.cluster_name
  location           = var.region
  initial_node_count = 1

  deletion_protection     = false
  remove_default_node_pool = true

  network    = "default"
  subnetwork = "default"

  logging_service    = "logging.googleapis.com/kubernetes"
  monitoring_service = "monitoring.googleapis.com/kubernetes"

  addons_config {
    http_load_balancing {
      disabled = false
    }
  }
}

# Create a node pool with auto-scaling enabled
resource "google_container_node_pool" "primary_nodes" {
  name     = var.node_pool_name
  cluster  = google_container_cluster.primary.name
  location = var.region
  node_count = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 15
    disk_type    = "pd-standard"
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform",
    ]
  }

  management {
    auto_upgrade = true
    auto_repair  = true
  }

  depends_on = [google_container_cluster.primary]
=======
=======
>>>>>>> ddb05319b4857cb0125430e0aaf5fac16212995f
  lifecycle {
    create_before_destroy = true
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "apache_server" {
  ami           = "ami-0df8c184d5f6ae949" # Amazon Linux 2 AMI (update if needed)
  instance_type = "t2.micro"
  key_name      = "key-gen" # Reference your existing key pair by name

  security_groups = [aws_security_group.flask_sg.name]

  iam_instance_profile = "access-to-s3" # Reference the existing IAM instance profile directly

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y git docker
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ec2-user
              newgrp docker
              yum install -y libxcrypt-compat

              curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose
              
              mkdir -p /home/ec2-user/flask-app
              git clone https://github.com/AmitayAlmog/flask-app.git /home/ec2-user/flask-app
              aws s3 cp s3://amitays-bucket/.env /home/ec2-user/flask-app/.env
              cd /home/ec2-user/flask-app
              
              docker-compose pull
              docker-compose up -d 
              EOF
}

output "instance_public_ip" {
  value       = aws_instance.apache_server.public_ip
  description = "Public IP of the EC2 instance"
<<<<<<< HEAD
>>>>>>> ddb05319b4857cb0125430e0aaf5fac16212995f
=======
>>>>>>> ddb05319b4857cb0125430e0aaf5fac16212995f
}
