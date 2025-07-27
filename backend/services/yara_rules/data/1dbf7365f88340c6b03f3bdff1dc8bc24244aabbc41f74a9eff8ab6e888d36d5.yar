rule auto_rule_20250726122317_3939 {
  strings:
    $o0 = "byte_4673E0" wide ascii nocase
  condition:
    all of them
}