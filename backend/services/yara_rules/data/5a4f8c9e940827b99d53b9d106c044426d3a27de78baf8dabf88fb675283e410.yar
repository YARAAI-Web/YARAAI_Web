rule auto_rule_20250726104533_8576 {
  strings:
    $o0 = "get_int_arg" wide ascii nocase
    $o1 = "GetStringTypeW" wide ascii nocase
    $o2 = "_cinit" wide ascii nocase
    $o3 = "stdargv" wide ascii nocase
    $o4 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    5 of ($o*)
}