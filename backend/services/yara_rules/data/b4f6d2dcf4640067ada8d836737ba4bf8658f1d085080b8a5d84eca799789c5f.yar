rule auto_rule_20250726190937_9435 {
  strings:
    $o0 = "CopyUnwindUp_0" wide ascii nocase
    $o1 = "off_450CD4" wide ascii nocase
  condition:
    all of them
}