rule auto_rule_20250727010726_5503 {
  strings:
    $o0 = "dword_783C0" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}