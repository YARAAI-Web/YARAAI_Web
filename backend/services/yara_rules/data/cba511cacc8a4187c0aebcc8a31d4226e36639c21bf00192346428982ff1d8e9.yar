rule auto_rule_20250726234155_7798 {
  strings:
    $o0 = "a0123456789abcd_3" wide ascii nocase
    $o1 = "m128i_i8" wide ascii nocase
    $o2 = "_Getgloballocale" wide ascii nocase
  condition:
    3 of ($o*)
}