rule auto_rule_20250726131519_4402 {
  strings:
    $o0 = "dword_450E84" wide ascii nocase
    $o1 = "overrun" wide ascii nocase
    $o2 = "dword_451130" wide ascii nocase
    $o3 = "fill_with_EOS_dwords" wide ascii nocase
  condition:
    4 of ($o*)
}