rule auto_rule_20250726135630_1560 {
  strings:
    $o0 = "dword_44E5E8" wide ascii nocase
    $o1 = "UnwindUp5_0" wide ascii nocase
  condition:
    all of them
}