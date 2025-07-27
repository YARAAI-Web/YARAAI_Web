rule auto_rule_20250727020258_3728 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "UnwindUp6_0" wide ascii nocase
    $o2 = "dword_4602B0" wide ascii nocase
  condition:
    3 of ($o*)
}