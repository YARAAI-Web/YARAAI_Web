rule auto_rule_20250726074824_7616 {
  strings:
    $o0 = "dword_4798DC" wide ascii nocase
  condition:
    all of them
}