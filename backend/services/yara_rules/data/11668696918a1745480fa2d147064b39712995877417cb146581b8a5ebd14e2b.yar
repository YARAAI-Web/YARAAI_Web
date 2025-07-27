rule auto_rule_20250726230113_5085 {
  strings:
    $o0 = "off_4017D4" wide ascii nocase
  condition:
    all of them
}