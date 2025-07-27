rule auto_rule_20250726143253_9999 {
  strings:
    $o0 = "dword_4690B8" wide ascii nocase
    $o1 = "word_4673F4" wide ascii nocase
  condition:
    all of them
}