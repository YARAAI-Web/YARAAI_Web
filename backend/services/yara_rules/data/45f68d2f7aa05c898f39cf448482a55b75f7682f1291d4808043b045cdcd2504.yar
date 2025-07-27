rule auto_rule_20250727004757_0898 {
  strings:
    $o0 = "byte_64030190" wide ascii nocase
  condition:
    all of them
}