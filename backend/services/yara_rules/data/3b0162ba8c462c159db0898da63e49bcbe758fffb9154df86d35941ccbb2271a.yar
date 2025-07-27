rule auto_rule_20250727010019_0892 {
  strings:
    $o0 = "find_end_of_dest_string_loop" wide ascii nocase
    $o1 = "dword_47251C" wide ascii nocase
    $o2 = "_onexit_lk" wide ascii nocase
  condition:
    3 of ($o*)
}