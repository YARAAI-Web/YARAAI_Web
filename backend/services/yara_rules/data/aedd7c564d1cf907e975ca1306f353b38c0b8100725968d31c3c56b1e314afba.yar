rule auto_rule_20250726222927_5558 {
  strings:
    $o0 = "dword_40CFD8" wide ascii nocase
    $o1 = "_set_statfp" wide ascii nocase
    $o2 = "UnwindUp2_0" wide ascii nocase
    $o3 = "x7FF" wide ascii nocase
  condition:
    4 of ($o*)
}