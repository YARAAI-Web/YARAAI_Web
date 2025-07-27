rule auto_rule_20250726072634_2704 {
  strings:
    $o0 = "find_end_of_dest_string_loop" wide ascii nocase
    $o1 = "dword_464404" wide ascii nocase
    $o2 = "off_463E64" wide ascii nocase
    $o3 = "dword_4643E0" wide ascii nocase
  condition:
    4 of ($o*)
}