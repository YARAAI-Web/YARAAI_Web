rule auto_rule_20250726145838_1934 {
  strings:
    $o0 = "dword_1400D1404" wide ascii nocase
    $o1 = "dword_1400D16C4" wide ascii nocase
  condition:
    all of them
}