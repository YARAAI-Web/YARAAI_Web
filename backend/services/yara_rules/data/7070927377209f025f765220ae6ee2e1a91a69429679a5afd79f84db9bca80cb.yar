rule auto_rule_20250726113140_9464 {
  strings:
    $o0 = "dword_456BFC" wide ascii nocase
    $o1 = "off_4181A0" wide ascii nocase
    $o2 = "dword_456BCC" wide ascii nocase
  condition:
    3 of ($o*)
}