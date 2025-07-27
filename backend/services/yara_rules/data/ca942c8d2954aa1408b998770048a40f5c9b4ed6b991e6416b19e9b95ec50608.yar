rule auto_rule_20250726060927_8179 {
  strings:
    $o0 = "_enable" wide ascii nocase
    $o1 = "word_1E926" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}