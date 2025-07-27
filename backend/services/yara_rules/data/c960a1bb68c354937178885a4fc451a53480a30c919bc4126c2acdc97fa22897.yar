rule auto_rule_20250726161138_8013 {
  strings:
    $o0 = "x7C5E" wide ascii nocase
  condition:
    all of them
}