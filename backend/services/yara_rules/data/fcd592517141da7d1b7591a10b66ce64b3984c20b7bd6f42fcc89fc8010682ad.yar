rule auto_rule_20250727014437_1830 {
  strings:
    $o0 = "lpDCB" wide ascii nocase
    $o1 = "fSearchOp" wide ascii nocase
  condition:
    all of them
}