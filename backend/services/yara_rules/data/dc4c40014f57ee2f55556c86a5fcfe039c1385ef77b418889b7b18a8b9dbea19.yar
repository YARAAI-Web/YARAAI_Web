rule auto_rule_20250726114629_4676 {
  strings:
    $o0 = "ppsEditable" wide ascii nocase
  condition:
    all of them
}