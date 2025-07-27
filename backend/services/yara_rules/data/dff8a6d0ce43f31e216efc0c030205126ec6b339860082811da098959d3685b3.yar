rule auto_rule_20250726134603_3683 {
  strings:
    $o0 = "x413B05" wide ascii nocase
  condition:
    all of them
}