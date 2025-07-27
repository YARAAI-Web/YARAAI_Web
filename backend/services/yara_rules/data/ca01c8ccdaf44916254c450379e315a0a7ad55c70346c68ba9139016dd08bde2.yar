rule auto_rule_20250726203308_4993 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "dword_410CC8" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
    $o3 = "dword_4111EC" wide ascii nocase
  condition:
    4 of ($o*)
}