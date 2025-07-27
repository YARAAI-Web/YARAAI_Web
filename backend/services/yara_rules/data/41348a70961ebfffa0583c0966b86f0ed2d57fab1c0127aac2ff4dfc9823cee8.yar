rule auto_rule_20250726112031_0659 {
  strings:
    $o0 = "x146" wide ascii nocase
    $o1 = "aQcapDL" wide ascii nocase
  condition:
    all of them
}