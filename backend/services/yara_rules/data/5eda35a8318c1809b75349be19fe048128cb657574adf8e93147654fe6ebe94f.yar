rule auto_rule_20250726185546_8561 {
  strings:
    $o0 = "x1E2A003272F3LL" wide ascii nocase
  condition:
    all of them
}