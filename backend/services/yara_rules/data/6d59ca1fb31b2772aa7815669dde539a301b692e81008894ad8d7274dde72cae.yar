rule auto_rule_20250726171421_8571 {
  strings:
    $o0 = "dword_40726C" wide ascii nocase
    $o1 = "x6C2" wide ascii nocase
    $o2 = "xDF2EFD7" wide ascii nocase
    $o3 = "x4292F0" wide ascii nocase
  condition:
    4 of ($o*)
}