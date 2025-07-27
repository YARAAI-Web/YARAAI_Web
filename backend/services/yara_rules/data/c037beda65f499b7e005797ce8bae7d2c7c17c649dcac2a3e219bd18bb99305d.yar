rule auto_rule_20250726154433_7204 {
  strings:
    $o0 = "word_1E61E" wide ascii nocase
    $o1 = "Object" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}