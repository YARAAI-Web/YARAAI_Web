rule auto_rule_20250726074717_8817 {
  strings:
    $o0 = "lpSecurityAttributes" wide ascii nocase
    $o1 = "off_402004" wide ascii nocase
  condition:
    all of them
}