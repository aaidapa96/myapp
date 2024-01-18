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
variable "vm_name" {
  description = "Name of the Azure Virtual Machine"
  type        = string
  default     = "aaidavm"
}

variable "admin_username" {
  description = "Admin username for the VM"
  type        = string
  default     = "aaidaabu"
}

variable "admin_password" {
  description = "Admin password for the VM"
  type        = string
  default     = "aaidaabu!12345"
}
