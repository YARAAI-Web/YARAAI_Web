rule auto_rule_20250726115424_1789 {
  strings:
    $o0 = "dword_4C129C" wide ascii nocase
  condition:
    all of them
}