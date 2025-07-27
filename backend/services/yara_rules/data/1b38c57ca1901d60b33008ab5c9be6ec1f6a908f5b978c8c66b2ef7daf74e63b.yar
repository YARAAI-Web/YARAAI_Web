rule auto_rule_20250726180817_7415 {
  strings:
    $o0 = "dword_472524" wide ascii nocase
  condition:
    all of them
}