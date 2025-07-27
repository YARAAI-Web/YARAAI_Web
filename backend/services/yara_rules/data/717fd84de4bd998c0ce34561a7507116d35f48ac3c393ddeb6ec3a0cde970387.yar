rule auto_rule_20250726215514_2719 {
  strings:
    $o0 = "dword_42EED4" wide ascii nocase
    $o1 = "dwShareMode" wide ascii nocase
  condition:
    all of them
}