rule auto_rule_20250726113812_4442 {
  strings:
    $o0 = "dword_7F6F0" wide ascii nocase
  condition:
    all of them
}