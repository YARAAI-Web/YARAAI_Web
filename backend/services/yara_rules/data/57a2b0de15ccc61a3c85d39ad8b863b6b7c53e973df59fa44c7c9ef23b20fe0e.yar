rule auto_rule_20250726174203_0550 {
  strings:
    $o0 = "dword_426EF5" wide ascii nocase
  condition:
    all of them
}