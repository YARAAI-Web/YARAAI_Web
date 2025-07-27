rule auto_rule_20250726150743_7940 {
  strings:
    $o0 = "x15100u" wide ascii nocase
  condition:
    all of them
}