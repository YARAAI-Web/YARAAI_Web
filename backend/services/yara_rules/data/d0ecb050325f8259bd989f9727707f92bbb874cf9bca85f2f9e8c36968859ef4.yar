rule auto_rule_20250726115946_3052 {
  strings:
    $o0 = "dword_43438E" wide ascii nocase
    $o1 = "dword_4326FC" wide ascii nocase
    $o2 = "CreateFontW" wide ascii nocase
  condition:
    3 of ($o*)
}