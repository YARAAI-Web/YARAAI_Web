rule auto_rule_20250726080236_4438 {
  strings:
    $o0 = "j_nullsub_3" wide ascii nocase
  condition:
    all of them
}