rule auto_rule_20250726182822_3585 {
  strings:
    $o0 = "off_64030540" wide ascii nocase
  condition:
    all of them
}