rule auto_rule_20250727020500_0665 {
  strings:
    $o0 = "byte_411FC0" wide ascii nocase
    $o1 = "TrailDown1_0" wide ascii nocase
  condition:
    all of them
}