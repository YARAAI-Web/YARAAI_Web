rule auto_rule_20250726083554_2385 {
  strings:
    $o0 = "_aulldiv" wide ascii nocase
    $o1 = "_pFirstBlock" wide ascii nocase
  condition:
    all of them
}