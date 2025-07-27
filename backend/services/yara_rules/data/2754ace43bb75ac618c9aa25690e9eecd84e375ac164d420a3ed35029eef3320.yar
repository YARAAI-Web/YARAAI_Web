rule auto_rule_20250727030110_4382 {
  strings:
    $o0 = "word_4304A2" wide ascii nocase
    $o1 = "dword_476980" wide ascii nocase
  condition:
    all of them
}