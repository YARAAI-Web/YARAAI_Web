rule auto_rule_20250726192043_1917 {
  strings:
    $o0 = "dword_4283EB" wide ascii nocase
    $o1 = "dword_42914B" wide ascii nocase
    $o2 = "off_428F4F" wide ascii nocase
  condition:
    3 of ($o*)
}