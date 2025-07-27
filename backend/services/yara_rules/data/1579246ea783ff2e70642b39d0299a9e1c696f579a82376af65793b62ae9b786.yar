rule auto_rule_20250726061714_7123 {
  strings:
    $o0 = "dword_4D1544" wide ascii nocase
    $o1 = "byte_4D1894" wide ascii nocase
  condition:
    all of them
}