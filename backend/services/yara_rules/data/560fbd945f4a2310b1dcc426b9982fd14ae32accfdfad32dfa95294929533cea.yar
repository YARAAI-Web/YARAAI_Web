rule auto_rule_20250727002116_5496 {
  strings:
    $o0 = "ResizePalette" wide ascii nocase
    $o1 = "PageSetupDlgW" wide ascii nocase
    $o2 = "dword_414B82" wide ascii nocase
  condition:
    3 of ($o*)
}