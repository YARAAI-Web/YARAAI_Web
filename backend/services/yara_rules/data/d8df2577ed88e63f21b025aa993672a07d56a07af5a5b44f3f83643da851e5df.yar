rule auto_rule_20250726232538_1387 {
  strings:
    $o0 = "dword_1400FF85C" wide ascii nocase
    $o1 = "dword_1400FF830" wide ascii nocase
    $o2 = "dword_1400FF8A4" wide ascii nocase
    $o3 = "dword_1400FF698" wide ascii nocase
  condition:
    4 of ($o*)
}