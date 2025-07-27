rule auto_rule_20250727041020_6228 {
  strings:
    $o0 = "dword_47566C" wide ascii nocase
    $o1 = "_ms_p5_test_fdiv" wide ascii nocase
  condition:
    all of them
}