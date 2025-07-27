rule auto_rule_20250726084816_6018 {
  strings:
    $o0 = "dword_427988" wide ascii nocase
    $o1 = "x19000u" wide ascii nocase
  condition:
    all of them
}