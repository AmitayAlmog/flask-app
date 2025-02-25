variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud Region"
  type        = string
}

variable "cluster_name" {
  description = "GKE Cluster Name"
  type        = string
}

variable "node_pool_name" {
  description = "GKE Node Pool Name"
  type        = string
}

variable "bucket_name" {
  description = "GCS Bucket Name for Terraform state"
  type        = string
}
