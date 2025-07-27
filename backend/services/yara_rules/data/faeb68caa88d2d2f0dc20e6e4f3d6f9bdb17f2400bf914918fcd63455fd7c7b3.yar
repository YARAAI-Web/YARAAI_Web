rule auto_rule_20250726072105_0822 {
  strings:
    $o0 = "dword_7EF08" wide ascii nocase
    $o1 = "dword_7F940" wide ascii nocase
  condition:
    all of them
}