rule auto_rule_20250726082859_8824 {
  strings:
    $o0 = "dword_42EEAC" wide ascii nocase
    $o1 = "dword_42EEBC" wide ascii nocase
    $o2 = "dword_42EECC" wide ascii nocase
  condition:
    3 of ($o*)
}