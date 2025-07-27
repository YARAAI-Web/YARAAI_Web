rule auto_rule_20250726153345_1963 {
  strings:
    $o0 = "dword_407800" wide ascii nocase
  condition:
    all of them
}