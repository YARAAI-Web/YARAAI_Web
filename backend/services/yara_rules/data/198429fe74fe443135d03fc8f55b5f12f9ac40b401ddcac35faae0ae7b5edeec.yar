rule auto_rule_20250726232427_4776 {
  strings:
    $o0 = "SnmpTfxClose" wide ascii nocase
    $o1 = "FindAtomA" wide ascii nocase
  condition:
    all of them
}