rule auto_rule_20250726214534_8834 {
  strings:
    $o0 = "lstrlenA" wide ascii nocase
    $o1 = "Calendar" wide ascii nocase
    $o2 = "dword_455638" wide ascii nocase
  condition:
    3 of ($o*)
}