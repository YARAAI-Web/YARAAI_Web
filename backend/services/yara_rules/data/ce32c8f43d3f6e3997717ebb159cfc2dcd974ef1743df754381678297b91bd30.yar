rule auto_rule_20250726175705_4809 {
  strings:
    $o0 = "off_4281EF" wide ascii nocase
  condition:
    all of them
}