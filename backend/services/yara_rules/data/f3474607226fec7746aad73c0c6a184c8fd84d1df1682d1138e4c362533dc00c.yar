rule auto_rule_20250727025039_5174 {
  strings:
    $o0 = "byte_40311B" wide ascii nocase
  condition:
    all of them
}