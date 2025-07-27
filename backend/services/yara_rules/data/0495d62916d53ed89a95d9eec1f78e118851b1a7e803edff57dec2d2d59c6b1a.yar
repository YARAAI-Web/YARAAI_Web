rule auto_rule_20250727005913_1506 {
  strings:
    $o0 = "dword_433760" wide ascii nocase
    $o1 = "x7FFFFFFFFFFFFFFFLL" wide ascii nocase
  condition:
    all of them
}