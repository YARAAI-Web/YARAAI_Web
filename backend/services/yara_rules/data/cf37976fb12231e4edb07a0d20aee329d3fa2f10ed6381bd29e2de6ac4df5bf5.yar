rule auto_rule_20250726190034_2928 {
  strings:
    $o0 = "__sbh_resize_block" wide ascii nocase
    $o1 = "dword_45CAC4" wide ascii nocase
    $o2 = "dword_42A020" wide ascii nocase
  condition:
    3 of ($o*)
}