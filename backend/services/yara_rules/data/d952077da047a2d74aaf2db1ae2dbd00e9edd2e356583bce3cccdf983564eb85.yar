rule auto_rule_20250726092147_1398 {
  strings:
    $o0 = "byte_73644" wide ascii nocase
  condition:
    all of them
}