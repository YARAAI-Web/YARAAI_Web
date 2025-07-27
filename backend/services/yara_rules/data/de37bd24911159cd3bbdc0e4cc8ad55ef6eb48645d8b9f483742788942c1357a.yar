rule auto_rule_20250727032834_2478 {
  strings:
    $o0 = "byte_1011F7A0" wide ascii nocase
  condition:
    all of them
}