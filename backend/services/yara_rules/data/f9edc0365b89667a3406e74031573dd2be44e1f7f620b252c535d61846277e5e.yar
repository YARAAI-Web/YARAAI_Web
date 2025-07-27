rule auto_rule_20250727031708_8516 {
  strings:
    $o0 = "then" wide ascii nocase
    $o1 = "http_gzip_static_module" wide ascii nocase
  condition:
    all of them
}