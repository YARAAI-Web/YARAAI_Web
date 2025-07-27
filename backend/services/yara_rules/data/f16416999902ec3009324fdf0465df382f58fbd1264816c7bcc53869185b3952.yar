rule auto_rule_20250726171316_6793 {
  strings:
    $o0 = "x6100000061LL" wide ascii nocase
    $o1 = "x3921226" wide ascii nocase
  condition:
    all of them
}