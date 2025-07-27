rule auto_rule_20250726161651_3937 {
  strings:
    $o0 = "dword_4C2188" wide ascii nocase
  condition:
    all of them
}