rule auto_rule_20250726070608_9157 {
  strings:
    $o0 = "LoadCursorA" wide ascii nocase
    $o1 = "dword_459A90" wide ascii nocase
    $o2 = "_ZeroTail" wide ascii nocase
    $o3 = "GdipDeleteFontFamily" wide ascii nocase
  condition:
    4 of ($o*)
}