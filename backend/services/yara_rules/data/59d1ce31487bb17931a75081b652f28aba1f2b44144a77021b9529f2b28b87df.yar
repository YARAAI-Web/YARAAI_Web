rule auto_rule_20250726130230_7272 {
  strings:
    $o0 = "off_476C34" wide ascii nocase
  condition:
    all of them
}