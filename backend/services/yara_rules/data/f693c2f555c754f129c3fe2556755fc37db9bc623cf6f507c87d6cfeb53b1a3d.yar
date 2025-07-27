rule auto_rule_20250726185838_7976 {
  strings:
    $o0 = "off_18012A090" wide ascii nocase
  condition:
    all of them
}