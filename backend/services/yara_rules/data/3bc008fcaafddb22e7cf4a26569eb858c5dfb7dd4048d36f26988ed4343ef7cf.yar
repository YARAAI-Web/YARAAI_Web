rule auto_rule_20250726185327_4170 {
  strings:
    $o0 = "x42000u" wide ascii nocase
    $o1 = "lpSecurityAttributes" wide ascii nocase
  condition:
    all of them
}