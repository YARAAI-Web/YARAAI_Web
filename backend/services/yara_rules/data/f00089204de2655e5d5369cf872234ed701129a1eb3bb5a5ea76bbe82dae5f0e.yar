rule auto_rule_20250726180535_6216 {
  strings:
    $o0 = "x999D" wide ascii nocase
  condition:
    all of them
}