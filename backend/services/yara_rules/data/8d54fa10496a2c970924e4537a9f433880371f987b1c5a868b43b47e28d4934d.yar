rule auto_rule_20250726225742_7552 {
  strings:
    $o0 = "word_781A8" wide ascii nocase
    $o1 = "word_1E54E" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}