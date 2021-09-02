
variable "api_id" {
  type        = string
  description = "ID for the API Gateway"
  default = "api-cfg4"
}

variable "api_config_id" {
  type        = string
  description = "ID for the API Gateway"
  default = "cfg4"
}

variable "path" {
  type        = string
  description = "Path for the YAML file with the API configuration"
  default = "petshopspec.yaml"
}

variable "project_id" {
}

variable "region" {
}
