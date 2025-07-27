rule auto_rule_20250726102720_2986 {
  strings:
    $o0 = "word_4CFC5C" wide ascii nocase
    $o1 = "word_4CFF94" wide ascii nocase
  condition:
    all of them
}