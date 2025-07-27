rule auto_rule_20250726070248_7461 {
  strings:
    $o0 = "dword_640303FC" wide ascii nocase
  condition:
    all of them
}