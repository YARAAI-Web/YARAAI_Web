rule auto_rule_20250727024825_9022 {
  strings:
    $o0 = "word_10147578" wide ascii nocase
    $o1 = "_Init_locks" wide ascii nocase
  condition:
    all of them
}