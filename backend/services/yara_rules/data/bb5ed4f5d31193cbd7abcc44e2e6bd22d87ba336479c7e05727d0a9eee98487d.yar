rule auto_rule_20250726060233_3811 {
  strings:
    $o0 = "fill_with_EOS_dwords" wide ascii nocase
    $o1 = "dword_475B54" wide ascii nocase
    $o2 = "overrun" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    4 of ($o*)
}