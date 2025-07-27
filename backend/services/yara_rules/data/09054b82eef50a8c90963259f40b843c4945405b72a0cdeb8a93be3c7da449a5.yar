rule auto_rule_20250726173313_6950 {
  strings:
    $o0 = "dword_40BE60" wide ascii nocase
    $o1 = "dword_40B5C4" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    3 of ($o*)
}