terraform {
  required_version = ">= 1.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "d0f2078d-2607-4c5e-a3d7-0e3c01f503a3"
}

resource "azurerm_resource_group" "devops" {
  name     = "rg-devops-cloud-dashboard"
  location = "southafricanorth"

  tags = {
    project     = "DevOps Cloud Status Dashboard"
    environment = "learning"
    managed_by  = "Terraform"
  }
}
