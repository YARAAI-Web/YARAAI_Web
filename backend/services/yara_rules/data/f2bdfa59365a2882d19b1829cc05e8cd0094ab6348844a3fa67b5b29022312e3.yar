rule auto_rule_20250726172811_8561 {
  strings:
    $o0 = "UnwindUp5_0" wide ascii nocase
    $o1 = "dword_42A008" wide ascii nocase
  condition:
    all of them
}