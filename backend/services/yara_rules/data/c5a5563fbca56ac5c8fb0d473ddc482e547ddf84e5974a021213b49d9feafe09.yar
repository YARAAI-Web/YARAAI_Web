rule auto_rule_20250726093408_7957 {
  strings:
    $o0 = "dword_4568EC" wide ascii nocase
    $o1 = "dword_455E00" wide ascii nocase
  condition:
    all of them
}