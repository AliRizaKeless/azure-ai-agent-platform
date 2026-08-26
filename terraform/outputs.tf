output "resource_group_name" {
  description = "Azure Resource Group name"
  value       = azurerm_resource_group.main.name
}

output "resource_group_location" {
  description = "Azure region where the Resource Group is deployed"
  value       = azurerm_resource_group.main.location
}

output "container_registry_name" {
  description = "Name of the Azure Container Registry"
  value       = azurerm_container_registry.main.name
}

output "container_registry_login_server" {
  description = "Azure Container Registry login server"
  value       = azurerm_container_registry.main.login_server
}

output "resource_group_id" {
  description = "Azure Resource Group resource ID"
  value       = azurerm_resource_group.main.id
}

output "container_registry_id" {
  description = "Azure Container Registry resource ID"
  value       = azurerm_container_registry.main.id
}

