resource "google_storage_bucket" "storage-bucket" {
  name          = var.name
  location      = "US"
  force_destroy = true
  project = var.project_id
}