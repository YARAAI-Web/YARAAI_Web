rule auto_rule_20250727044256_2692 {
  strings:
    $o0 = "aGsyst12111cgcr" wide ascii nocase
    $o1 = "dword_42EECC" wide ascii nocase
  condition:
    all of them
}