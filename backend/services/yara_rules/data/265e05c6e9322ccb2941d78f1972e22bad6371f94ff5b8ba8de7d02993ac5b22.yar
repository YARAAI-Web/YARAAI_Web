rule auto_rule_20250726212322_1843 {
  strings:
    $o0 = "dword_783D0" wide ascii nocase
    $o1 = "dword_78420" wide ascii nocase
  condition:
    all of them
}