rule auto_rule_20250726085809_6242 {
  strings:
    $o0 = "x5A1EADE003272FALL" wide ascii nocase
    $o1 = "x420311" wide ascii nocase
  condition:
    all of them
}