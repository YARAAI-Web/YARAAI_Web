rule auto_rule_20250726121413_9038 {
  strings:
    $o0 = "lParam2" wide ascii nocase
  condition:
    all of them
}