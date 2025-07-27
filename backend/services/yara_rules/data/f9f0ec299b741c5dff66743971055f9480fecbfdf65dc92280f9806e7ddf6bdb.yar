rule auto_rule_20250726115520_2188 {
  strings:
    $o0 = "byte_64029308" wide ascii nocase
    $o1 = "byte_64028950" wide ascii nocase
  condition:
    all of them
}