rule auto_rule_20250726104343_5364 {
  strings:
    $o0 = "x24C7" wide ascii nocase
  condition:
    all of them
}