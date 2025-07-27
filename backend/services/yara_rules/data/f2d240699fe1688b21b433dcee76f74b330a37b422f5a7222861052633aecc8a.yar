rule auto_rule_20250726223215_8010 {
  strings:
    $o0 = "dword_64031488" wide ascii nocase
  condition:
    all of them
}