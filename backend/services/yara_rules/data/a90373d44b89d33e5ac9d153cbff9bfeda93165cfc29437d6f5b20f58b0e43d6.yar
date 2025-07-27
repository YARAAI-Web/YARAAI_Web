rule auto_rule_20250727043003_2483 {
  strings:
    $o0 = "off_1802EE300" wide ascii nocase
  condition:
    all of them
}