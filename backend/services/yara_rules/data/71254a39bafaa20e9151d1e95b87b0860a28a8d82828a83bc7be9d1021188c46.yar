rule auto_rule_20250726230144_1610 {
  strings:
    $o0 = "dword_40F018" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
  condition:
    all of them
}