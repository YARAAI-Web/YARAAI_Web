rule auto_rule_20250726123743_0794 {
  strings:
    $o0 = "_itoa" wide ascii nocase
    $o1 = "dword_463A18" wide ascii nocase
  condition:
    all of them
}