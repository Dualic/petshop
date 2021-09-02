
resource "google_api_gateway_api" "api_cfg4" {
  provider = google-beta
  api_id = var.api_id
  project = var.project_id
}

resource "google_api_gateway_api_config" "api_cfg4" {
  provider = google-beta
  api = google_api_gateway_api.api_cfg4.api_id
  api_config_id = var.api_config_id
  project = var.project_id

  openapi_documents {
    document {
      path = var.path
      contents = filebase64("petshopspec.yaml")
    }
  }
  lifecycle {
    create_before_destroy = true
  }
}

resource "google_api_gateway_gateway" "api_cfg4" {
  provider = google-beta
  api_config = google_api_gateway_api_config.api_cfg4.id
  gateway_id = "api-gw4"
  project = var.project_id
  region = var.region
}