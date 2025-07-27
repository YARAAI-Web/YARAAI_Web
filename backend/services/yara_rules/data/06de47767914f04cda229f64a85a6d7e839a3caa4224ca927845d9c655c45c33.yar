rule auto_rule_20250726060209_8279 {
  strings:
    $o0 = "byte_4D1362" wide ascii nocase
  condition:
    all of them
}