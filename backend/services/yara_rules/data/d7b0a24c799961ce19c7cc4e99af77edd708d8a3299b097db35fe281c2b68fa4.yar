rule auto_rule_20250726175335_2879 {
  strings:
    $o0 = "dword_1400C7514" wide ascii nocase
  condition:
    all of them
}