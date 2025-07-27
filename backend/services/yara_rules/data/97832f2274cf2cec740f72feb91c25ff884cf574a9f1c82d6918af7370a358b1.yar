rule auto_rule_20250726175345_0092 {
  strings:
    $o0 = "loader_1_0" wide ascii nocase
  condition:
    all of them
}