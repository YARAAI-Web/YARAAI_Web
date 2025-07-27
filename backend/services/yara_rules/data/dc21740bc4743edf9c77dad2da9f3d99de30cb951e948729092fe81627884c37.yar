rule auto_rule_20250726075147_2573 {
  strings:
    $o0 = "dword_4C1328" wide ascii nocase
    $o1 = "dword_4C12A4" wide ascii nocase
  condition:
    all of them
}