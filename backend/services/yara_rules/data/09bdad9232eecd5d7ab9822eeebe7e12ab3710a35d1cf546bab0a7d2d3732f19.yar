rule auto_rule_20250726205921_9339 {
  strings:
    $o0 = "dbgrpt" wide ascii nocase
  condition:
    all of them
}