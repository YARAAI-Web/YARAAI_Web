rule auto_rule_20250726133928_2280 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "dword_782E4" wide ascii nocase
  condition:
    all of them
}