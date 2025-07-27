rule auto_rule_20250726180407_4121 {
  strings:
    $o0 = "off_1400D9000" wide ascii nocase
    $o1 = "dword_1400DB7F0" wide ascii nocase
  condition:
    all of them
}