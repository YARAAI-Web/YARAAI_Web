rule auto_rule_20250726092105_1494 {
  strings:
    $o0 = "ppsEditable" wide ascii nocase
  condition:
    all of them
}