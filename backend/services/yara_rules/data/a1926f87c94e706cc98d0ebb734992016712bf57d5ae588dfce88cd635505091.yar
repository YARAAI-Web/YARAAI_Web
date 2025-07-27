rule auto_rule_20250727010028_1552 {
  strings:
    $o0 = "off_474A58" wide ascii nocase
    $o1 = "off_474A4C" wide ascii nocase
  condition:
    all of them
}