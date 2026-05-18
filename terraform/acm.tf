# Issue the cert
resource "aws_acm_certificate" "main" {
  count             = var.domain_name != "" ? 1 : 0
  domain_name       = var.domain_name
  validation_method = "DNS"
  lifecycle {
    create_before_destroy = true
  }
}

# Add the validation CNAME to Cloudflare automatically
resource "cloudflare_dns_record" "acm_validation" {
  for_each = length(aws_acm_certificate.main) > 0 ? {
    for dvo in aws_acm_certificate.main[0].domain_validation_options : dvo.domain_name => dvo
  } : {}

  zone_id = var.cloudflare_zone_id
  name    = each.value.resource_record_name
  content = each.value.resource_record_value
  type    = each.value.resource_record_type
  ttl     = 60
  proxied = false
}

# Validate the cert once the DNS record is in place
resource "aws_acm_certificate_validation" "main" {
  count                   = var.domain_name != "" ? 1 : 0
  certificate_arn         = aws_acm_certificate.main[0].arn
  validation_record_fqdns = [for record in cloudflare_dns_record.acm_validation : record.hostname]

  timeouts {
    create = "10m"
  }
}
