rule auto_rule_20250727012035_8035 {
  strings:
    $o0 = "_ms_p5_test_fdiv" wide ascii nocase
    $o1 = "dword_457A48" wide ascii nocase
  condition:
    all of them
}