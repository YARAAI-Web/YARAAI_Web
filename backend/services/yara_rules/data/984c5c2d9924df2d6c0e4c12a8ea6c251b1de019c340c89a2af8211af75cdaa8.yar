rule auto_rule_20250726170213_5615 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}