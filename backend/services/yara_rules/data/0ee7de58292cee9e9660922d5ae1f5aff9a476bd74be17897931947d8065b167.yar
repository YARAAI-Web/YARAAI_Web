rule auto_rule_20250726074921_3457 {
  strings:
    $o0 = "asc_405130" wide ascii nocase
  condition:
    all of them
}