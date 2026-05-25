variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-north-1"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "ecommerce-app"
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["eu-north-1a", "eu-north-1b"]
}

variable "container_port" {
  description = "Port exposed by the container"
  type        = number
  default     = 8000
}

variable "DB_NAME" {
  description = "Database name"
  type        = string
  default     = "storefront3"
}

variable "DB_USER" {
  description = "Database username"
  type        = string
  default     = "storefront_user"
}

variable "DB_PORT" {
  description = "Database port"
  type        = string
  default     = "3306"
}



variable "DB_PASSWORD" {
  description = "Database master password"
  type        = string
  sensitive   = true
}

variable "ecs_task_cpu" {
  description = "Fargate task CPU units"
  type        = string
  default     = "256"
}

variable "ecs_task_memory" {
  description = "Fargate task memory in MB"
  type        = string
  default     = "512"
}

variable "desired_count" {
  description = "Number of ECS tasks to run"
  type        = number
  default     = 2
}

variable "health_check_path" {
  description = "Health check endpoint"
  type        = string
  default     = "/health/"
}

variable "domain_name" {
  description = "Domain name for the application (app.ziadco.com)"
  type        = string
  default     = "app.ziadco.com"
}

# variable "route53_zone_name" {
#   description = "Route 53 hosted zone name (app.ziadco.com)"
#   type        = string
#   default     = "app.ziadco.com"
# }

# variable "create_route53_record" {
#   description = "Whether to create Route 53 DNS record"
#   type        = bool
#   default     = false
# }


variable "cloudflare_api_token" {
  description = "Cloudflare API token for DNS management (if using Cloudflare)"
  type        = string
  sensitive   = true
  default     = ""
}

variable "cloudflare_zone_id" {
  description = "Cloudflare zone ID for the domain (if using Cloudflare)"
  type        = string
  sensitive   = true
  default     = ""
}

variable "cloudflare_account_id" {
  description = "Cloudflare account ID (if using Cloudflare)"
  type        = string
  sensitive   = true
  default     = ""
}

variable "secret_key" {
  description = "Django secret key"
  type        = string
  sensitive   = true
  default     = ""
}
variable "SUPERUSER_NAME" {
  description = "Django superuser name"
  type        = string
  sensitive   = true
  default     = ""
}

variable "SUPERUSER_EMAIL" {
  description = "Django superuser email"
  type        = string
  sensitive   = true
  default     = ""
}

variable "SUPERUSER_PASSWORD" {
  description = "Django superuser password"
  type        = string
  sensitive   = true
  default     = ""
}

