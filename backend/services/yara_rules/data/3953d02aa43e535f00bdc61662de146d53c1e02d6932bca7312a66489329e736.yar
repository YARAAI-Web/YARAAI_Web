rule auto_rule_20250726065436_8938 {
  strings:
    $o0 = "dword_A61FC4" wide ascii nocase
  condition:
    all of them
}