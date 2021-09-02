terraform {
  backend "gcs" {
    bucket  = "week10-1-324606"
 prefix  = "terraform/state"
  }
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 3.45.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file)
}

provider "google-beta" {
  credentials = file(var.credentials_file)
}

module "storage" {
  source     = ".//modules/storage"
  region = var.region
  project_id = var.project_id
}

module "database" {
  source = ".//modules/database"
  region = var.region
  project_id = var.project_id
  password = var.password
}

module "functions" {
  source = ".//modules/functions"
  region = var.region
  project_id = var.project_id
}

module "gateway" {
  source = ".//modules/gateway"
  project_id = var.project_id
  region = var.region
}

