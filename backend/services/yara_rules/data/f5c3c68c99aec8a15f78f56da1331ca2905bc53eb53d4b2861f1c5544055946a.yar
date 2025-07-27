rule auto_rule_20250726064845_4533 {
  strings:
    $o0 = "x1FFFF" wide ascii nocase
    $o1 = "dword_45940C" wide ascii nocase
  condition:
    all of them
}