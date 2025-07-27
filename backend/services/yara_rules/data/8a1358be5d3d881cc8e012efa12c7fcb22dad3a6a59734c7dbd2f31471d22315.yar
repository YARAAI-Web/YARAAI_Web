rule auto_rule_20250726224241_5114 {
  strings:
    $o0 = "xFEDu" wide ascii nocase
    $o1 = "leaks" wide ascii nocase
  condition:
    all of them
}