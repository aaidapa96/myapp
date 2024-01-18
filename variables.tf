variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "aaida_rg"
}

variable "location" {
  description = "Azure region where the Resource Group will be created"
  type        = string
  default     = "centralindia"
}
