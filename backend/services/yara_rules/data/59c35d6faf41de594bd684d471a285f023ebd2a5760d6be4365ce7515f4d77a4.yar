rule auto_rule_20250726085448_7916 {
  strings:
    $o0 = "dword_6402E98C" wide ascii nocase
  condition:
    all of them
}