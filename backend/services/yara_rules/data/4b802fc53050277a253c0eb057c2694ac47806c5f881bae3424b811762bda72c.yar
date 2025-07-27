rule auto_rule_20250726095926_6843 {
  strings:
    $o0 = "dword_4D31C4" wide ascii nocase
  condition:
    all of them
}