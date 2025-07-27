rule auto_rule_20250726223251_4623 {
  strings:
    $o0 = "dword_411D40" wide ascii nocase
    $o1 = "dword_411D74" wide ascii nocase
    $o2 = "dword_4118F0" wide ascii nocase
  condition:
    3 of ($o*)
}