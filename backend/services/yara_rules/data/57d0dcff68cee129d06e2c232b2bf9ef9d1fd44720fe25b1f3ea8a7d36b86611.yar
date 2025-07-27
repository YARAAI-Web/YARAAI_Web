rule auto_rule_20250726095938_8452 {
  strings:
    $o0 = "dword_40BCFC" wide ascii nocase
    $o1 = "ReturnValue" wide ascii nocase
    $o2 = "_ms_p5_test_fdiv" wide ascii nocase
  condition:
    3 of ($o*)
}