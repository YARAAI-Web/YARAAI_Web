rule auto_rule_20250726114535_8700 {
  strings:
    $o0 = "xFFFFE092" wide ascii nocase
  condition:
    all of them
}