rule auto_rule_20250726133753_9703 {
  strings:
    $o0 = "dword_412274" wide ascii nocase
    $o1 = "dword_411F2C" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    3 of ($o*)
}