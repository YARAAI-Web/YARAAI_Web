rule auto_rule_20250727005936_5346 {
  strings:
    $o0 = "dword_45CEF8" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
    $o2 = "UnwindUp0_0" wide ascii nocase
  condition:
    3 of ($o*)
}