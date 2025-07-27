rule auto_rule_20250726174646_2301 {
  strings:
    $o0 = "dword_46428C" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
    $o2 = "fill_with_EOS_dwords" wide ascii nocase
    $o3 = "TrailUp0_0" wide ascii nocase
  condition:
    4 of ($o*)
}