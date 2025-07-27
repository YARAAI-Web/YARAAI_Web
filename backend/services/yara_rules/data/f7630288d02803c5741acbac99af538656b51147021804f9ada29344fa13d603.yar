rule auto_rule_20250726231851_8770 {
  strings:
    $o0 = "dword_64031488" wide ascii nocase
  condition:
    all of them
}