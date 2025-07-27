rule auto_rule_20250726114351_6439 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
    $o2 = "dword_45FE30" wide ascii nocase
    $o3 = "_nh_malloc" wide ascii nocase
    $o4 = "_global_unwind2" wide ascii nocase
  condition:
    5 of ($o*)
}