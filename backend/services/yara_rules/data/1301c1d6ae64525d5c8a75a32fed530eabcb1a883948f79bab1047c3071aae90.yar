rule auto_rule_20250726142231_6895 {
  strings:
    $o0 = "_ioinit" wide ascii nocase
    $o1 = "xFEDu" wide ascii nocase
  condition:
    all of them
}