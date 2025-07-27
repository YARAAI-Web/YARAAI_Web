rule auto_rule_20250726072028_7611 {
  strings:
    $o0 = "x26D2829" wide ascii nocase
  condition:
    all of them
}