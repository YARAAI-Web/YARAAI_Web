rule auto_rule_20250726181426_5410 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}