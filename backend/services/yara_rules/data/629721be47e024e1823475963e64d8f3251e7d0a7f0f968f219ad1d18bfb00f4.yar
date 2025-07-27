rule auto_rule_20250726203022_6917 {
  strings:
    $o0 = "dword_412AF0" wide ascii nocase
  condition:
    all of them
}