rule auto_rule_20250726234939_5528 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "x413B05" wide ascii nocase
  condition:
    all of them
}