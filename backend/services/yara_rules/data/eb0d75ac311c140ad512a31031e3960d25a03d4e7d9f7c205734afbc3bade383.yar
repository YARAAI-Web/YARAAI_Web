rule auto_rule_20250726184414_3765 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "dword_455CBC" wide ascii nocase
  condition:
    all of them
}