rule auto_rule_20250726153615_2573 {
  strings:
    $o0 = "dwCreationDisposition" wide ascii nocase
    $o1 = "word_418244" wide ascii nocase
  condition:
    all of them
}