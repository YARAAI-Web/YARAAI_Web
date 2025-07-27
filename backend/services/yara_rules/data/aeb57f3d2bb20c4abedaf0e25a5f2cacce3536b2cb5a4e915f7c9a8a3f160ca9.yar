rule auto_rule_20250726100207_5928 {
  strings:
    $o0 = "finish_loop" wide ascii nocase
    $o1 = "dword_476AAC" wide ascii nocase
  condition:
    all of them
}