rule auto_rule_20250726183959_1467 {
  strings:
    $o0 = "dwErrCodea" wide ascii nocase
    $o1 = "hObjectb" wide ascii nocase
  condition:
    all of them
}