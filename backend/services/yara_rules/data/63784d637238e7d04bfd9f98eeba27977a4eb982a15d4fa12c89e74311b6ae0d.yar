rule auto_rule_20250726224418_6088 {
  strings:
    $o0 = "x314E" wide ascii nocase
    $o1 = "aLgc2R8cNng" wide ascii nocase
    $o2 = "dword_42D01C" wide ascii nocase
    $o3 = "x7510896u" wide ascii nocase
  condition:
    4 of ($o*)
}