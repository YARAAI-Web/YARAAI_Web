rule auto_rule_20250726213525_5902 {
  strings:
    $o0 = "dword_41B1A8" wide ascii nocase
  condition:
    all of them
}