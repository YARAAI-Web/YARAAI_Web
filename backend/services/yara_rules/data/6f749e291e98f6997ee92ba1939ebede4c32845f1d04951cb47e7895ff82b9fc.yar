rule auto_rule_20250726220140_8290 {
  strings:
    $o0 = "LoadCursorFromFileW" wide ascii nocase
    $o1 = "nBuff" wide ascii nocase
    $o2 = "lpPoints" wide ascii nocase
    $o3 = "MessageBoxIndirectW" wide ascii nocase
  condition:
    4 of ($o*)
}