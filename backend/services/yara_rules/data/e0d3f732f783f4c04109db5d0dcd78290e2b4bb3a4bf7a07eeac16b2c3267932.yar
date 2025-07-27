rule auto_rule_20250727035042_1522 {
  strings:
    $o0 = "dword_45D8A8" wide ascii nocase
    $o1 = "byte_45D681" wide ascii nocase
    $o2 = "dword_45D500" wide ascii nocase
    $o3 = "find_end_of_dest_string_loop" wide ascii nocase
    $o4 = "dword_45D8B4" wide ascii nocase
  condition:
    4 of ($o*)
}