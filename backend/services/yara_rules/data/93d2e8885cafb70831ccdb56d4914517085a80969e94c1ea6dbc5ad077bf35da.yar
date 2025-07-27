rule auto_rule_20250726065328_9543 {
  strings:
    $o0 = "dword_463A24" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
    $o3 = "off_4640F0" wide ascii nocase
  condition:
    4 of ($o*)
}