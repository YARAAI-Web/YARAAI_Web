rule auto_rule_20250726115552_1421 {
  strings:
    $o0 = "aHidffd1c" wide ascii nocase
  condition:
    all of them
}