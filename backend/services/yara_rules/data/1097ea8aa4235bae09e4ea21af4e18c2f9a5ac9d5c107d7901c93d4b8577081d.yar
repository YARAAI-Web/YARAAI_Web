rule auto_rule_20250727044620_5638 {
  strings:
    $o0 = "off_428361" wide ascii nocase
    $o1 = "x23FF" wide ascii nocase
    $o2 = "C12h" wide ascii nocase
    $o3 = "dword_42840D" wide ascii nocase
    $o4 = "dword_4282FD" wide ascii nocase
  condition:
    4 of ($o*)
}