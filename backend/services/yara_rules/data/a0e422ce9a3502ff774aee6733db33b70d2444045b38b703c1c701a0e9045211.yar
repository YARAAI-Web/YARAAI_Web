rule auto_rule_20250727003640_3047 {
  strings:
    $o0 = "dword_427E08" wide ascii nocase
    $o1 = "dword_424000" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    3 of ($o*)
}