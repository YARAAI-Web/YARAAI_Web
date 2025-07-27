rule auto_rule_20250726192515_8987 {
  strings:
    $o0 = "word_40707A" wide ascii nocase
    $o1 = "byte_410520" wide ascii nocase
    $o2 = "byte_407081" wide ascii nocase
  condition:
    3 of ($o*)
}