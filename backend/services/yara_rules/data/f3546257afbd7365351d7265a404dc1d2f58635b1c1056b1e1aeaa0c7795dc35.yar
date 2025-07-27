rule auto_rule_20250726215435_8753 {
  strings:
    $o0 = "x561425" wide ascii nocase
    $o1 = "_mm_cmpeq_epi8" wide ascii nocase
    $o2 = "off_74D04C" wide ascii nocase
  condition:
    3 of ($o*)
}