rule auto_rule_20250726130430_2755 {
  strings:
    $o0 = "dword_418040" wide ascii nocase
    $o1 = "_isctype" wide ascii nocase
    $o2 = "_ms_p5_mp_test_fdiv" wide ascii nocase
    $o3 = "_NLG_Notify" wide ascii nocase
    $o4 = "dword_4183F8" wide ascii nocase
  condition:
    4 of ($o*)
}