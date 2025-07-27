rule auto_rule_20250727032327_6466 {
  strings:
    $o0 = "x70F182" wide ascii nocase
  condition:
    all of them
}