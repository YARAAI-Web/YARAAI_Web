rule auto_rule_20250726151134_5257 {
  strings:
    $o0 = "dword_4061CD" wide ascii nocase
  condition:
    all of them
}