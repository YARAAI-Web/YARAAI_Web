rule auto_rule_20250726184151_1877 {
  strings:
    $o0 = "before" wide ascii nocase
    $o1 = "off_466AEC" wide ascii nocase
  condition:
    all of them
}