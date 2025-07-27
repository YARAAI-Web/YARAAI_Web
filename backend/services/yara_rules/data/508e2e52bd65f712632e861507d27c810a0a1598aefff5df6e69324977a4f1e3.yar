rule auto_rule_20250726164100_2267 {
  strings:
    $o0 = "off_4A9044" wide ascii nocase
  condition:
    all of them
}