rule auto_rule_20250726093010_4640 {
  strings:
    $o0 = "dword_4642C4" wide ascii nocase
  condition:
    all of them
}