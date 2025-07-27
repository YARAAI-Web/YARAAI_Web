rule auto_rule_20250726154841_7237 {
  strings:
    $o0 = "off_42601C" wide ascii nocase
    $o1 = "dword_426648" wide ascii nocase
  condition:
    all of them
}