rule auto_rule_20250726100051_1887 {
  strings:
    $o0 = "ulOptions" wide ascii nocase
    $o1 = "cchItemText" wide ascii nocase
    $o2 = "hTemplateFile" wide ascii nocase
    $o3 = "lpKeyState" wide ascii nocase
  condition:
    4 of ($o*)
}