rule auto_rule_20250726103244_7840 {
  strings:
    $o0 = "x8A32" wide ascii nocase
  condition:
    all of them
}