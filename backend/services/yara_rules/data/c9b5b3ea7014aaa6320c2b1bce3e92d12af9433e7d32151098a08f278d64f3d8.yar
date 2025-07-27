rule auto_rule_20250726165603_1681 {
  strings:
    $o0 = "off_49DDB8" wide ascii nocase
    $o1 = "dword_4C1298" wide ascii nocase
  condition:
    all of them
}