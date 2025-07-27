rule auto_rule_20250726073347_1419 {
  strings:
    $o0 = "off_7E404" wide ascii nocase
    $o1 = "word_1DE6E" wide ascii nocase
  condition:
    all of them
}