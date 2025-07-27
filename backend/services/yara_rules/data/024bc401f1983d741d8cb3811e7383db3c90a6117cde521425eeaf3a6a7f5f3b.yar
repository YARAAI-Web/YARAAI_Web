rule auto_rule_20250726224103_6819 {
  strings:
    $o0 = "dword_426068" wide ascii nocase
  condition:
    all of them
}