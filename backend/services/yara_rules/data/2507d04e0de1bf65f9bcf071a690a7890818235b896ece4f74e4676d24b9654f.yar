rule auto_rule_20250726225319_6152 {
  strings:
    $o0 = "x5408" wide ascii nocase
    $o1 = "dword_4335CB" wide ascii nocase
    $o2 = "HidePointerOriginal" wide ascii nocase
    $o3 = "dword_433657" wide ascii nocase
  condition:
    4 of ($o*)
}