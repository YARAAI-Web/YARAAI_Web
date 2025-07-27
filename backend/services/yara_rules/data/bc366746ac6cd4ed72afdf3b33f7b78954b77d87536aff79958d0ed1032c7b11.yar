rule auto_rule_20250726123633_1192 {
  strings:
    $o0 = "dword_1400C7548" wide ascii nocase
  condition:
    all of them
}