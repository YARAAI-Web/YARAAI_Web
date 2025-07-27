rule auto_rule_20250727030934_2941 {
  strings:
    $o0 = "dword_467EA4" wide ascii nocase
  condition:
    all of them
}