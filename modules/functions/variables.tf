
variable "name" {
  type        = list(string)
  default = ["cartadd", "cartdelete", "cartdeleteall", "cartgetall", "cartupdate", "checkout", "createtables", "customeradd", "customerdelete",
  "customergetall", "customerupdate", "productadd", "productdelete", "productgetall", "productupdate", "warehouseadd", "warehousedelete",
  "warehouseget", "warehousegetall", "warehouseupdate"]
  description = "The name to apply to any nameable resources."
}

variable "description" {
  type        = string
  default     = "Processes events."
  description = "The description of the function."
}

variable "runtime" {
  type        = string
  default     = "python39"
  description = "The runtime in which the function will be executed."
}

variable "entry_point" {
  type        = list(string)
  default = ["cartadd", "cartdelete", "cartdeleteall", "cartgetall", "cartupdate", "checkout", "createtables", "customeradd", "customerdelete",
  "customergetall", "customerupdate", "productadd", "productdelete", "productgetall", "productupdate", "warehouseadd", "warehousedelete",
  "warehouseget", "warehousegetall", "warehouseupdate"]
  description = "The name of a method in the function source which will be invoked when the function is executed."
}

variable "environment_variables" {
  type        = map(string)
  default     = {}
  description = "A set of key/value environment variable pairs to assign to the function."
}

variable "source_repository_url" {
  type        = string
  default = list["https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/cartadd",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/cartdelete",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/cartdeleteall",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/cartgetall",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/cartupdate",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/checkout",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/createtables",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/customeradd",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/customerdelete",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/customergetall",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/customerupdate",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/productadd",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/productdelete",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/productgetall",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/productupdate",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/warehouseadd",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/warehousedelete",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/warehouseget",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/warehousegetall",
  "https://source.developers.google.com/projects/week10-1-324606/repos/github_dualic_petshop/moveable-aliases/master/paths/functions/warehouseupdate"
  ]

  description = "The URL of the repository which contains the function source code."
}

variable "region" {
}

variable "project_id" {
}