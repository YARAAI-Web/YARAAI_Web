rule auto_rule_20250726181740_5971 {
  strings:
    $o0 = "off_44BF70" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
  condition:
    all of them
}