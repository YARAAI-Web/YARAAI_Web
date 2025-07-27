rule auto_rule_20250726125841_1294 {
  strings:
    $o0 = "chkesp" wide ascii nocase
    $o1 = "dword_423001" wide ascii nocase
  condition:
    all of them
}