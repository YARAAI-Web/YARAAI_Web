rule auto_rule_20250726132420_6703 {
  strings:
    $o0 = "dword_450000" wide ascii nocase
    $o1 = "fill_with_EOS_dwords" wide ascii nocase
    $o2 = "UnwindUp5_0" wide ascii nocase
  condition:
    3 of ($o*)
}