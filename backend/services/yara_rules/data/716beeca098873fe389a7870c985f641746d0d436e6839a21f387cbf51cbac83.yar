rule auto_rule_20250726214026_1767 {
  strings:
    $o0 = "InvertRect" wide ascii nocase
    $o1 = "SetCursorPos" wide ascii nocase
    $o2 = "x17000u" wide ascii nocase
    $o3 = "bMenu" wide ascii nocase
    $o4 = "DialogBoxParamW" wide ascii nocase
  condition:
    4 of ($o*)
}