rule auto_rule_20250726074042_5688 {
  strings:
    $o0 = "dword_403344" wide ascii nocase
  condition:
    all of them
}