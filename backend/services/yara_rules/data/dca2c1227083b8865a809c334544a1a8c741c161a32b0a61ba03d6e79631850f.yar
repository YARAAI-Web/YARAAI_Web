rule auto_rule_20250726223511_1111 {
  strings:
    $o0 = "dword_412248" wide ascii nocase
    $o1 = "dword_411900" wide ascii nocase
    $o2 = "dword_411EE4" wide ascii nocase
  condition:
    3 of ($o*)
}