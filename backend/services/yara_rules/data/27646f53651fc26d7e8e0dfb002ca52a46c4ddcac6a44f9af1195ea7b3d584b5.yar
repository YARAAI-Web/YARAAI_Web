rule auto_rule_20250726210928_8529 {
  strings:
    $o0 = "dword_7E5C0" wide ascii nocase
    $o1 = "dword_7FA80" wide ascii nocase
  condition:
    all of them
}