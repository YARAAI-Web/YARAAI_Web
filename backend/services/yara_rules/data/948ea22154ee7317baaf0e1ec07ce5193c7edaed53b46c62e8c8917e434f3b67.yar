rule auto_rule_20250726193850_8231 {
  strings:
    $o0 = "saturated_mul" wide ascii nocase
    $o1 = "dword_10097DD8" wide ascii nocase
  condition:
    all of them
}