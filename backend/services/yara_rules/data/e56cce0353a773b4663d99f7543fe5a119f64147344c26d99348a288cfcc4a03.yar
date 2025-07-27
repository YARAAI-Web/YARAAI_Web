rule auto_rule_20250726063643_1235 {
  strings:
    $o0 = "j_unknown_libname_153" wide ascii nocase
    $o1 = "j____current_exception" wide ascii nocase
    $o2 = "big_integer" wide ascii nocase
  condition:
    3 of ($o*)
}