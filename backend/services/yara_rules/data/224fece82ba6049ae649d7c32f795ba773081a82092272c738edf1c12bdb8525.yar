rule auto_rule_20250726135955_2826 {
  strings:
    $o0 = "dword_449EE8" wide ascii nocase
    $o1 = "dword_449AB0" wide ascii nocase
    $o2 = "dword_449EAC" wide ascii nocase
  condition:
    3 of ($o*)
}