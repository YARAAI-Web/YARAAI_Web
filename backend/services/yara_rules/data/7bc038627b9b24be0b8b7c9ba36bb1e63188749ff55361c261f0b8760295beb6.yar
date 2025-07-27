rule auto_rule_20250727002707_9137 {
  strings:
    $o0 = "dword_4561F0" wide ascii nocase
    $o1 = "dword_455E5C" wide ascii nocase
    $o2 = "UnwindUp6_0" wide ascii nocase
  condition:
    3 of ($o*)
}