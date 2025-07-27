rule auto_rule_20250726110928_3505 {
  strings:
    $o0 = "dword_44E5DC" wide ascii nocase
    $o1 = "ProcessWindowStation" wide ascii nocase
    $o2 = "off_44D578" wide ascii nocase
    $o3 = "dword_44E438" wide ascii nocase
    $o4 = "find_end_of_dest_string_loop" wide ascii nocase
  condition:
    4 of ($o*)
}