rule auto_rule_20250726183338_5781 {
  strings:
    $o0 = "word_4513D0" wide ascii nocase
    $o1 = "_msize" wide ascii nocase
  condition:
    all of them
}