
provider "cloudflare" {
  api_token = var.cloudflare_api_token
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

