
resource "google_sql_database_instance" "petshopdb" {
  name             = "petshop-instance3"
  root_password = "root"
  database_version = "POSTGRES_13"
  region           = var.region
  project = var.project_id
  
  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled = true
      authorized_networks {
        name = "all"
        value = "0.0.0.0/0"
      }
    }
  }
}

resource "google_sql_user" "finaluser" {
  name     = "finaluser"
  instance = "petshop-instance3"
  password = var.password
  project = var.project_id
  depends_on = [
    google_sql_database_instance.petshopdb
  ]
}

resource "google_sql_database" "finaldb" {
  name     = "finaldb"
  instance = "petshop-instance3"
  project = var.project_id
  depends_on = [
    google_sql_database_instance.petshopdb
  ]
}