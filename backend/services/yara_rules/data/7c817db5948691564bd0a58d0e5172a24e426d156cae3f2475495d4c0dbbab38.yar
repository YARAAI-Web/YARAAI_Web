rule auto_rule_20250726173804_4990 {
  strings:
    $o0 = "dword_4D3124" wide ascii nocase
    $o1 = "x1DAE" wide ascii nocase
  condition:
    all of them
}