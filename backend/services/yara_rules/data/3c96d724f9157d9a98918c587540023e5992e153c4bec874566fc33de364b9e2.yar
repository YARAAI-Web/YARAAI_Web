rule auto_rule_20250726151103_5425 {
  strings:
    $o0 = "dword_42A8A5" wide ascii nocase
    $o1 = "dword_42A7ED" wide ascii nocase
    $o2 = "off_42A8B1" wide ascii nocase
  condition:
    3 of ($o*)
}