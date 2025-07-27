rule auto_rule_20250726110045_5644 {
  strings:
    $o0 = "off_11075C0C" wide ascii nocase
  condition:
    all of them
}