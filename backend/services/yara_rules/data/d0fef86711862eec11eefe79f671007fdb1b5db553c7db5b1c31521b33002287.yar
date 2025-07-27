rule auto_rule_20250726173556_1489 {
  strings:
    $o0 = "dword_6402E990" wide ascii nocase
  condition:
    all of them
}