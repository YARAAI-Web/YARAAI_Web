rule auto_rule_20250726134437_0535 {
  strings:
    $o0 = "dword_41DA98" wide ascii nocase
    $o1 = "aClnnd1ef948800" wide ascii nocase
    $o2 = "x17000u" wide ascii nocase
    $o3 = "LoadCursorA" wide ascii nocase
  condition:
    4 of ($o*)
}