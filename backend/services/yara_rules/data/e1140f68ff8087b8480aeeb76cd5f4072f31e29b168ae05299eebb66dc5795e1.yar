rule auto_rule_20250726235920_3018 {
  strings:
    $o0 = "dword_4794D4" wide ascii nocase
  condition:
    all of them
}