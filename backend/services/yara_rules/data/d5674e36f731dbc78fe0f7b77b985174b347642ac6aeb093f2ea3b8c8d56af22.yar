rule auto_rule_20250726092004_4347 {
  strings:
    $o0 = "dword_78988" wide ascii nocase
  condition:
    all of them
}