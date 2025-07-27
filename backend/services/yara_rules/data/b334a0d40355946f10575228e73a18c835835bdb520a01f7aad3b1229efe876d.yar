rule auto_rule_20250727030415_0687 {
  strings:
    $o0 = "dword_78414" wide ascii nocase
    $o1 = "dword_78114" wide ascii nocase
  condition:
    all of them
}