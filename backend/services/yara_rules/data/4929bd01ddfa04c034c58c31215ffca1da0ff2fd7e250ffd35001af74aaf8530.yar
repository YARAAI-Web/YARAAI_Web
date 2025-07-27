rule auto_rule_20250726132338_1133 {
  strings:
    $o0 = "dword_411D5C" wide ascii nocase
  condition:
    all of them
}