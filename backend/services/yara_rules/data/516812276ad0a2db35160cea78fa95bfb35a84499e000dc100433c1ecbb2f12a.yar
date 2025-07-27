rule auto_rule_20250726230655_1007 {
  strings:
    $o0 = "dword_1400DB564" wide ascii nocase
    $o1 = "dword_1400DB6EC" wide ascii nocase
    $o2 = "dword_1400DB9B0" wide ascii nocase
  condition:
    3 of ($o*)
}