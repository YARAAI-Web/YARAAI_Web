rule auto_rule_20250726212724_2389 {
  strings:
    $o0 = "xFFFFB6F6" wide ascii nocase
  condition:
    all of them
}