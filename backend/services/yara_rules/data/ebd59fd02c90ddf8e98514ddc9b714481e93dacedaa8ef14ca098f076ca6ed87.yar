rule auto_rule_20250726134519_4503 {
  strings:
    $o0 = "dword_77F78" wide ascii nocase
  condition:
    all of them
}