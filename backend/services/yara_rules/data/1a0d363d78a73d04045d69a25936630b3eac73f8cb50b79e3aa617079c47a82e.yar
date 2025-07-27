rule auto_rule_20250726102007_1029 {
  strings:
    $o0 = "CascadeWindows" wide ascii nocase
    $o1 = "x17000u" wide ascii nocase
    $o2 = "ClipCursor" wide ascii nocase
    $o3 = "MenuItemFromPoint" wide ascii nocase
  condition:
    4 of ($o*)
}