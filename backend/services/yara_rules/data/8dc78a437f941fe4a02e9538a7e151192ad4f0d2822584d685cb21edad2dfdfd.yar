rule auto_rule_20250726104728_1108 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "dword_44C174" wide ascii nocase
    $o2 = "dword_44C4E0" wide ascii nocase
  condition:
    3 of ($o*)
}