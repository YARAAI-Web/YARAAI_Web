rule auto_rule_20250726073549_1876 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "_ms_p5_mp_test_fdiv" wide ascii nocase
    $o2 = "byte_4673C6" wide ascii nocase
    $o3 = "subtype" wide ascii nocase
  condition:
    4 of ($o*)
}