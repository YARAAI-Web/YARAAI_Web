rule auto_rule_20250726223531_1609 {
  strings:
    $o0 = "dword_10003144" wide ascii nocase
    $o1 = "ResourceA" wide ascii nocase
    $o2 = "FileA" wide ascii nocase
  condition:
    3 of ($o*)
}