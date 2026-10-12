# DevOps Cloud Status Dashboard

## Overview

This project demonstrates a practical DevOps workflow for building, testing, containerizing, and preparing a Python web application for cloud deployment on Microsoft Azure.

It is being developed incrementally to demonstrate hands-on skills in cloud engineering, Infrastructure as Code (IaC), CI/CD, containers, and application operations.

## Technology Stack

- **Application:** Python and Flask
- **Web server:** Gunicorn
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Infrastructure as Code:** Terraform
- **Cloud platform:** Microsoft Azure
- **Version control:** Git and GitHub

## Current Features

- Flask web application with application and health-check endpoints.
- Docker image built from a Python slim base image.
- Non-root user configured for running the application inside the container.
- Docker health check configured to monitor application availability.
- Automated application tests using pytest.
- GitHub Actions workflow for testing and building the Docker image.
- Terraform configuration for managing an Azure resource group.
- Terraform outputs for retrieving the Azure resource group's name and location.

## Azure Infrastructure

Terraform manages the following Azure resource:

| Resource | Name or value |
|---|---|
| Resource type | Azure Resource Group |
| Resource group | `rg-devops-cloud-dashboard` |
| Region | `southafricanorth` |
| Infrastructure management | Terraform |

The resource group has been created and verified. No virtual machines, databases, or Kubernetes clusters have been deployed as part of the current stage.

## Project Structure

```text
devops-cloud-project/
├── app/
│   └── main.py
├── tests/
│   └── test_app.py
├── terraform/
│   ├── main.tf
│   └── .terraform.lock.hcl
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Useful Commands

Run application tests:

```bash
pytest
```

Build the Docker image:

```bash
docker build -t devops-cloud-dashboard .
```

Initialize Terraform:

```bash
terraform -chdir=terraform init
```

Validate the Terraform configuration:

```bash
terraform -chdir=terraform validate
```

Preview infrastructure changes:

```bash
terraform -chdir=terraform plan
```

View Terraform outputs:

```bash
terraform -chdir=terraform output
```

Review the Terraform plan carefully before applying changes to Azure. Cloud resources may incur charges.

## Planned Improvements

- Improve the dashboard interface and application functionality.
- Add deployment automation.
- Evaluate affordable Azure hosting options.
- Introduce monitoring, logging, and security improvements.
- Explore Kubernetes deployment where appropriate.

## Project Status

**Current stage:** Application containerization, automated CI, and Terraform-managed Azure infrastructure.

**Status:** In progress.

## Learning Objectives

This project is intended to demonstrate practical experience with Git, Linux, Python, Docker, automated testing, GitHub Actions, Terraform, Microsoft Azure, troubleshooting, and cloud deployment practices.
