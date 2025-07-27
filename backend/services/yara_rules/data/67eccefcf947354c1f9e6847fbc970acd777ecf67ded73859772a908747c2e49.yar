rule auto_rule_20250726104829_2580 {
  strings:
    $o0 = "xFFFFF4C7" wide ascii nocase
  condition:
    all of them
}