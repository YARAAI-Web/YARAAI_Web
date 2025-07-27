rule auto_rule_20250726072814_3249 {
  strings:
    $o0 = "xFFLL" wide ascii nocase
  condition:
    all of them
}