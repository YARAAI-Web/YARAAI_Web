rule auto_rule_20250726122731_1499 {
  strings:
    $o0 = "dword_46A0BC" wide ascii nocase
    $o1 = "xC0000093" wide ascii nocase
  condition:
    all of them
}