variable "location" {
  description = "Azure deployment region"
  default     = "norwayeast"
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
}

variable "container_registry_sku" {
  description = "Azure Container Registry SKU"
  default     = "Basic"
}