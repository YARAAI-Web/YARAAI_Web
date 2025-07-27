rule auto_rule_20250726071745_6624 {
  strings:
    $o0 = "fill_with_EOS_dwords" wide ascii nocase
    $o1 = "dword_44C154" wide ascii nocase
    $o2 = "program" wide ascii nocase
    $o3 = "acmDriverClose" wide ascii nocase
  condition:
    4 of ($o*)
}