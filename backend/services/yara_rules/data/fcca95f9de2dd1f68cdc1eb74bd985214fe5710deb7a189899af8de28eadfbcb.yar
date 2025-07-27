rule auto_rule_20250726094038_7682 {
  strings:
    $o0 = "GUIResizeMode" wide ascii nocase
    $o1 = "String1e" wide ascii nocase
    $o2 = "TrayOnEventMode" wide ascii nocase
    $o3 = "dword_4C115C" wide ascii nocase
    $o4 = "dword_4C16B0" wide ascii nocase
  condition:
    4 of ($o*)
}