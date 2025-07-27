rule auto_rule_20250726171526_5617 {
  strings:
    $o0 = "x3F000u" wide ascii nocase
  condition:
    all of them
}