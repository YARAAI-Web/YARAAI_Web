rule auto_rule_20250726173826_6381 {
  strings:
    $o0 = "dword_78194" wide ascii nocase
  condition:
    all of them
}