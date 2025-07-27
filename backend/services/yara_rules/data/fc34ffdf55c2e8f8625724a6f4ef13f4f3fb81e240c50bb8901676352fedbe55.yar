rule auto_rule_20250726075517_3683 {
  strings:
    $o0 = "byte_640301F3" wide ascii nocase
  condition:
    all of them
}