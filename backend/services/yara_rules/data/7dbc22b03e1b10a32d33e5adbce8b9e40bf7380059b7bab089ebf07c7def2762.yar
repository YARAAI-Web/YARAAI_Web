rule auto_rule_20250726203853_8967 {
  strings:
    $o0 = "byte_6402E068" wide ascii nocase
  condition:
    all of them
}