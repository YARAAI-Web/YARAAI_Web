rule auto_rule_20250727014109_4478 {
  strings:
    $o0 = "dword_4C15EC" wide ascii nocase
    $o1 = "MapVirtualKeyW" wide ascii nocase
    $o2 = "byte_4BB500" wide ascii nocase
  condition:
    3 of ($o*)
}