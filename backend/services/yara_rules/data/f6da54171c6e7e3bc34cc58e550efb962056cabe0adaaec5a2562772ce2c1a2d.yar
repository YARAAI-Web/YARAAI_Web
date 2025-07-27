rule auto_rule_20250726195910_1438 {
  strings:
    $o0 = "dword_46854C" wide ascii nocase
    $o1 = "word_4E10E0" wide ascii nocase
  condition:
    all of them
}