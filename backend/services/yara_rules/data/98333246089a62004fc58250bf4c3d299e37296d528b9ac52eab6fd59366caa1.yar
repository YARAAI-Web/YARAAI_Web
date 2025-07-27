rule auto_rule_20250726222224_7426 {
  strings:
    $o0 = "dword_428EA5" wide ascii nocase
    $o1 = "x70941F8A" wide ascii nocase
  condition:
    all of them
}