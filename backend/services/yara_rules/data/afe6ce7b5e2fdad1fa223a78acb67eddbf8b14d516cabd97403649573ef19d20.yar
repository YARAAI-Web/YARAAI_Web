rule auto_rule_20250726203756_0807 {
  strings:
    $o0 = "byte_403059" wide ascii nocase
    $o1 = "byte_403057" wide ascii nocase
  condition:
    all of them
}