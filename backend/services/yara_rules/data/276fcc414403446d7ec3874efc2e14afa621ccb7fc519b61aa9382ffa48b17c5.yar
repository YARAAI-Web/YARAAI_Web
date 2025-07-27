rule auto_rule_20250726185523_0760 {
  strings:
    $o0 = "dword_417E49" wide ascii nocase
    $o1 = "dword_40D6A8" wide ascii nocase
    $o2 = "x4012u" wide ascii nocase
  condition:
    3 of ($o*)
}