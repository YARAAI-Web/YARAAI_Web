rule auto_rule_20250726165710_6755 {
  strings:
    $o0 = "dword_4060F8" wide ascii nocase
    $o1 = "SetKeyboardState" wide ascii nocase
    $o2 = "lstrlenA" wide ascii nocase
  condition:
    3 of ($o*)
}