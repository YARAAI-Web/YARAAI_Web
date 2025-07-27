rule auto_rule_20250726174455_0750 {
  strings:
    $o0 = "FFF4h" wide ascii nocase
  condition:
    all of them
}