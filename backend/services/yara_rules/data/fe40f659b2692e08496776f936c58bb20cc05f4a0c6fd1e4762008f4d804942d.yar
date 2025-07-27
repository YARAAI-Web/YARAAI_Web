rule auto_rule_20250726101017_1374 {
  strings:
    $o0 = "x312u" wide ascii nocase
    $o1 = "dword_4C5A34" wide ascii nocase
  condition:
    all of them
}