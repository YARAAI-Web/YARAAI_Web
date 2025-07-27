rule auto_rule_20250726190731_6014 {
  strings:
    $o0 = "off_457320" wide ascii nocase
  condition:
    all of them
}