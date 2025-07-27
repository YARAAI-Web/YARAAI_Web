rule auto_rule_20250727002840_8190 {
  strings:
    $o0 = "off_4698C0" wide ascii nocase
  condition:
    all of them
}