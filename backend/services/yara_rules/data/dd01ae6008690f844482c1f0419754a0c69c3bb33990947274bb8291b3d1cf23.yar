rule auto_rule_20250726191255_5614 {
  strings:
    $o0 = "fill_with_EOS_dwords" wide ascii nocase
    $o1 = "dword_45D264" wide ascii nocase
    $o2 = "dword_42A028" wide ascii nocase
  condition:
    3 of ($o*)
}