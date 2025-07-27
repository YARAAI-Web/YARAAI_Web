rule auto_rule_20250726150248_9632 {
  strings:
    $o0 = "_ms_p5_test_fdiv" wide ascii nocase
    $o1 = "dword_456CC8" wide ascii nocase
    $o2 = "UnwindUp3_0" wide ascii nocase
  condition:
    3 of ($o*)
}