rule auto_rule_20250726103853_5952 {
  strings:
    $o0 = "dword_456C84" wide ascii nocase
    $o1 = "UnwindUp3_0" wide ascii nocase
    $o2 = "_cfltcvt_init" wide ascii nocase
  condition:
    3 of ($o*)
}