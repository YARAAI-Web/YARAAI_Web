rule auto_rule_20250726235728_0931 {
  strings:
    $o0 = "dword_1400D13A0" wide ascii nocase
  condition:
    all of them
}