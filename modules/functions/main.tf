
resource "google_cloudfunctions_function" "function" {
  project = var.project_id
  region = var.region
  name        = var.name[count.index]
  description = var.description
  runtime     = var.runtime
  available_memory_mb   = 256
  count = 20
  entry_point           = var.entry_point[count.index]
  trigger_http          = true
  
  #environment_variables = var.environment_variables

  source_repository {
    url = var.source_repository_url[count.index]
  }
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  count = 2
  project        = google_cloudfunctions_function.function[count.index].project
  region         = google_cloudfunctions_function.function[count.index].region
  cloud_function = google_cloudfunctions_function.function[count.index].name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}