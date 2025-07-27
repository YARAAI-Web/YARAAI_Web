rule auto_rule_20250726195220_5905 {
  strings:
    $o0 = "dwErrCodeb" wide ascii nocase
    $o1 = "hObjectb" wide ascii nocase
  condition:
    all of them
}