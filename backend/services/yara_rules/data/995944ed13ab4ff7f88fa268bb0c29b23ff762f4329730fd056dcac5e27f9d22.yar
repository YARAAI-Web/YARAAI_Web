rule auto_rule_20250726183007_1311 {
  strings:
    $o0 = "byte_48B8FB" wide ascii nocase
  condition:
    all of them
}