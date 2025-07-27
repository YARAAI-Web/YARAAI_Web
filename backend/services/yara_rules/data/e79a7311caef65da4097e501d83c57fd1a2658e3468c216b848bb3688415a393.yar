rule auto_rule_20250726223758_0666 {
  strings:
    $o0 = "off_4B2C80" wide ascii nocase
  condition:
    all of them
}