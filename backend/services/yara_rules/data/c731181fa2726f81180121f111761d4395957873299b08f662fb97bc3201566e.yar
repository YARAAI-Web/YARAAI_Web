rule auto_rule_20250726135250_4305 {
  strings:
    $o0 = "dword_45CACC" wide ascii nocase
    $o1 = "dword_45CB08" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
    $o3 = "_SEH_epilog" wide ascii nocase
    $o4 = "strpbrk" wide ascii nocase
  condition:
    4 of ($o*)
}