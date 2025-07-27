rule auto_rule_20250726135619_6033 {
  strings:
    $o0 = "x49D6" wide ascii nocase
    $o1 = "dword_428565" wide ascii nocase
    $o2 = "off_4283B1" wide ascii nocase
  condition:
    3 of ($o*)
}