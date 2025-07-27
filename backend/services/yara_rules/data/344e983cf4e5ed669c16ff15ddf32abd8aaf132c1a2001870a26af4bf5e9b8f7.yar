rule auto_rule_20250726232449_5782 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}