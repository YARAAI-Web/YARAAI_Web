rule auto_rule_20250726175254_7091 {
  strings:
    $o0 = "x7AD3" wide ascii nocase
    $o1 = "dword_42FC2E" wide ascii nocase
  condition:
    all of them
}