rule auto_rule_20250726085941_4951 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "x15Eu" wide ascii nocase
  condition:
    all of them
}