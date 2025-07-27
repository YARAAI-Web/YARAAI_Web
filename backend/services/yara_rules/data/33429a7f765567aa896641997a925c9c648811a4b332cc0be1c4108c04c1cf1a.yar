rule auto_rule_20250726171515_3389 {
  strings:
    $o0 = "nFilterType" wide ascii nocase
  condition:
    all of them
}