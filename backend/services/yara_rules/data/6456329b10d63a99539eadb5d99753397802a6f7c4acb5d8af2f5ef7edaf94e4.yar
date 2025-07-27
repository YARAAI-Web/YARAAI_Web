rule auto_rule_20250726082252_2037 {
  strings:
    $o0 = "dword_4D3130" wide ascii nocase
  condition:
    all of them
}