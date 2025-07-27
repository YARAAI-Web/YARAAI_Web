rule auto_rule_20250726215304_6147 {
  strings:
    $o0 = "o9FItIX" wide ascii nocase
    $o1 = "off_447038" wide ascii nocase
  condition:
    all of them
}