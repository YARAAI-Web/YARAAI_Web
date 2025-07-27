rule auto_rule_20250726235807_3287 {
  strings:
    $o0 = "dword_4767D0" wide ascii nocase
  condition:
    all of them
}