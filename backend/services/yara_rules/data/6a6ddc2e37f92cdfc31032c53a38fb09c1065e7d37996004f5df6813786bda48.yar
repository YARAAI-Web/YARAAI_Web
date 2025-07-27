rule auto_rule_20250726153512_1425 {
  strings:
    $o0 = "dword_457E00" wide ascii nocase
    $o1 = "_ms_p5_mp_test_fdiv" wide ascii nocase
  condition:
    all of them
}