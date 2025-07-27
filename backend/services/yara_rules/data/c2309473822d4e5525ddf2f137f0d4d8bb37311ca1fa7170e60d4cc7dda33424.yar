rule auto_rule_20250726150724_0807 {
  strings:
    $o0 = "byte_4671D4" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
    $o2 = "off_466EF4" wide ascii nocase
    $o3 = "main_loop_start" wide ascii nocase
    $o4 = "_ioinit" wide ascii nocase
  condition:
    4 of ($o*)
}