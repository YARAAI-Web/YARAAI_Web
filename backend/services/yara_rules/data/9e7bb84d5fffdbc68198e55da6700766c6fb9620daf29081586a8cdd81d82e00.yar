rule auto_rule_20250726062539_3770 {
  strings:
    $o0 = "x5E0ABF" wide ascii nocase
  condition:
    all of them
}