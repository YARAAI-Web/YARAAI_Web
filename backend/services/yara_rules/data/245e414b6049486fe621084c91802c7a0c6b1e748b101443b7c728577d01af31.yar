rule auto_rule_20250726145609_7779 {
  strings:
    $o0 = "dword_640303E8" wide ascii nocase
  condition:
    all of them
}