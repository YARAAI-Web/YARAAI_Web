rule auto_rule_20250726060524_5635 {
  strings:
    $o0 = "byte_4507D8" wide ascii nocase
    $o1 = "OpenMutexA" wide ascii nocase
  condition:
    all of them
}