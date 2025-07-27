rule auto_rule_20250726211022_6767 {
  strings:
    $o0 = "byte_64028540" wide ascii nocase
  condition:
    all of them
}