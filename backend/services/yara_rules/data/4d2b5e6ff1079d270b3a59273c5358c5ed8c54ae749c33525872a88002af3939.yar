rule auto_rule_20250726124757_5246 {
  strings:
    $o0 = "off_476C64" wide ascii nocase
    $o1 = "find_end_of_dest_string_loop" wide ascii nocase
    $o2 = "dword_477484" wide ascii nocase
  condition:
    3 of ($o*)
}