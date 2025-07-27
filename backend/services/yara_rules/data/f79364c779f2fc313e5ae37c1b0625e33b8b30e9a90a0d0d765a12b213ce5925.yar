rule auto_rule_20250726222413_0587 {
  strings:
    $o0 = "D3Eh" wide ascii nocase
  condition:
    all of them
}