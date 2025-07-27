rule auto_rule_20250727032246_4956 {
  strings:
    $o0 = "off_4027E4" wide ascii nocase
  condition:
    all of them
}