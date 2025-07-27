rule auto_rule_20250726063149_9355 {
  strings:
    $o0 = "x417800" wide ascii nocase
    $o1 = "dword_4767DC" wide ascii nocase
    $o2 = "UnwindUp2_0" wide ascii nocase
  condition:
    3 of ($o*)
}