rule auto_rule_20250726144219_8185 {
  strings:
    $o0 = "x4036C1" wide ascii nocase
  condition:
    all of them
}