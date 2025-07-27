rule auto_rule_20250726214448_5042 {
  strings:
    $o0 = "dword_4C115C" wide ascii nocase
    $o1 = "off_49DC2C" wide ascii nocase
  condition:
    all of them
}