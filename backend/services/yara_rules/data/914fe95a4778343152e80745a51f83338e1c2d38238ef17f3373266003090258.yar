rule auto_rule_20250726165928_2171 {
  strings:
    $o0 = "TrailDown0_0" wide ascii nocase
    $o1 = "byte_4652E0" wide ascii nocase
  condition:
    all of them
}