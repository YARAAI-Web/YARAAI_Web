rule auto_rule_20250726065111_4291 {
  strings:
    $o0 = "WindowFromDC" wide ascii nocase
    $o1 = "SetDlgItemInt" wide ascii nocase
    $o2 = "hWndRemove" wide ascii nocase
    $o3 = "LoadKeyboardLayoutA" wide ascii nocase
  condition:
    4 of ($o*)
}