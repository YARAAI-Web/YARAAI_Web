rule auto_rule_20250726164959_8132 {
  strings:
    $o0 = "lstrcatW" wide ascii nocase
    $o1 = "x19000u" wide ascii nocase
  condition:
    all of them
}