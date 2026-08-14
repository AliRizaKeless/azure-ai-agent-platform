variable "location" {
  description = "Azure deployment region"
  type        = string
  default     = "norwayeast"
  nullable    = false

  validation {
    condition     = contains(["norwayeast", "westeurope"], var.location)
    error_message = "Location must be either 'norwayeast' or 'westeurope'."
  }
}

variable "resource_group_name" {
  description = "Azure Resource Group name"
  type        = string
  default     = "rg-ai-agent-platform"
  nullable    = false

  validation {
    condition     = length(trimspace(var.resource_group_name)) > 0
    error_message = "Resource Group name cannot be empty."
  }
}

variable "container_app_environment_name" {
  default = "env-ai-agent-platform"
}

variable "container_registry_name" {
  description = "Azure Container Registry name"
  type        = string
  default     = "acraliagentplatform"

  validation {
    condition     = can(regex("^[a-zA-Z0-9]{5,50}$", var.container_registry_name))
    error_message = "Container Registry name must be 5-50 alphanumeric characters."
  }
}

variable "container_registry_admin_enabled" {
  description = "Enable admin user for Azure Container Registry"
  type        = bool
  default     = true
}

variable "project_name" {
  description = "Project name used for Azure resources"
  type        = string
  default     = "azure-ai-agent-platform"

  validation {
    condition     = length(var.project_name) > 0
    error_message = "Project name cannot be empty."
  }
}

variable "container_registry_sku" {
  description = "Azure Container Registry SKU"
  default     = "Basic"

  validation {
    condition     = contains(["Basic", "Standard", "Premium"], var.container_registry_sku)
    error_message = "Container Registry SKU must be Basic, Standard, or Premium."
  }
}