variable "location" {
  description = "Azure deployment region"
  default     = "norwayeast"

  validation {
    condition     = contains(["norwayeast", "westeurope"], var.location)
    error_message = "Location must be either 'norwayeast' or 'westeurope'."
  }
}

variable "resource_group_name" {
  description = "Azure Resource Group name"
  default     = "rg-ai-agent-platform"
}

variable "container_app_environment_name" {
  default = "env-ai-agent-platform"
}

variable "container_registry_name" {
  default = "acraliagentplatform"
}

variable "project_name" {
  description = "Project name used for Azure resources"
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