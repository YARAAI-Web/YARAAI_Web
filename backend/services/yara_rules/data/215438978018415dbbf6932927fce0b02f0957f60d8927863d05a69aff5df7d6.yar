rule auto_rule_20250726140933_1978 {
  strings:
    $o0 = "dword_435DB6" wide ascii nocase
    $o1 = "lpOutputFunc" wide ascii nocase
  condition:
    all of them
}