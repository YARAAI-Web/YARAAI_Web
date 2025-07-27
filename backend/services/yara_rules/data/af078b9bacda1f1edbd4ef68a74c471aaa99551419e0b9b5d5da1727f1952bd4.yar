rule auto_rule_20250726111746_9305 {
  strings:
    $o0 = "report_failure" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
    $o3 = "dword_444C64" wide ascii nocase
  condition:
    4 of ($o*)
}