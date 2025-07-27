rule auto_rule_20250726134354_4785 {
  strings:
    $o0 = "dword_40B018" wide ascii nocase
    $o1 = "dword_449EA8" wide ascii nocase
    $o2 = "dword_44A3AC" wide ascii nocase
  condition:
    3 of ($o*)
}