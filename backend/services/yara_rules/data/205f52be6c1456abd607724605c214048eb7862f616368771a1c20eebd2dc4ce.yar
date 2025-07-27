rule auto_rule_20250726073740_1771 {
  strings:
    $o0 = "dword_403118" wide ascii nocase
  condition:
    all of them
}