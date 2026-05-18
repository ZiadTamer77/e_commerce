
provider "cloudflare" {
  api_token = var.cloudflare_api_token
}


# Enable TLS 1.3
resource "cloudflare_zone_setting" "tls_1_3" {
  zone_id    = var.cloudflare_zone_id
  setting_id = "tls_1_3"
  value      = "on"
}

# Enable automatic HTTPS rewrites
resource "cloudflare_zone_setting" "automatic_https_rewrites" {
  zone_id    = var.cloudflare_zone_id
  setting_id = "automatic_https_rewrites"
  value      = "on"
}

# Set SSL mode to strict
resource "cloudflare_zone_setting" "ssl" {
  zone_id    = var.cloudflare_zone_id
  setting_id = "ssl"
  value      = "strict"
}

resource "cloudflare_dns_record" "app" {
  zone_id = var.cloudflare_zone_id
  name    = "app"
  content = aws_lb.main.dns_name
  type    = "CNAME"
  ttl     = 1
  proxied = true
  comment = "Domain verification record"
}

