rule auto_rule_20250726143642_0579 {
  strings:
    $o0 = "x36Au" wide ascii nocase
    $o1 = "CreatePopupMenu" wide ascii nocase
    $o2 = "SetCommBreak" wide ascii nocase
    $o3 = "dword_428020" wide ascii nocase
  condition:
    4 of ($o*)
}