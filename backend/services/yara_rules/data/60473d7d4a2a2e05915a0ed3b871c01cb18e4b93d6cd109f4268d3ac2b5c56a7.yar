rule auto_rule_20250726230450_1070 {
  strings:
    $o0 = "dword_45D8B8" wide ascii nocase
    $o1 = "x_ismbbtype" wide ascii nocase
    $o2 = "program" wide ascii nocase
    $o3 = "UnwindUp1_0" wide ascii nocase
  condition:
    4 of ($o*)
}