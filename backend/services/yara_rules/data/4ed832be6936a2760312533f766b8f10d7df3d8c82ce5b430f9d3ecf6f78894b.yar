rule auto_rule_20250726134814_8898 {
  strings:
    $o0 = "x3E7D" wide ascii nocase
    $o1 = "dword_4325F4" wide ascii nocase
    $o2 = "x4C17" wide ascii nocase
  condition:
    3 of ($o*)
}