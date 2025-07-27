rule auto_rule_20250727032750_8049 {
  strings:
    $o0 = "dword_78420" wide ascii nocase
  condition:
    all of them
}