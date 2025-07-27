rule auto_rule_20250726225731_0826 {
  strings:
    $o0 = "ppsEditable" wide ascii nocase
  condition:
    all of them
}