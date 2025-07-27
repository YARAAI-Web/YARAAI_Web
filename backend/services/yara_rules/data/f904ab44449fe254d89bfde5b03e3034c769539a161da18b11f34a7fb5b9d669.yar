rule auto_rule_20250726223555_5496 {
  strings:
    $o0 = "EnumResourceNamesW" wide ascii nocase
    $o1 = "word_4C2100" wide ascii nocase
  condition:
    all of them
}