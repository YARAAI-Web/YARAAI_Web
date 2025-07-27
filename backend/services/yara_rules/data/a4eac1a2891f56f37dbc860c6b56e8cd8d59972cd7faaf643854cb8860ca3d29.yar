rule auto_rule_20250727035615_0738 {
  strings:
    $o0 = "word_492918" wide ascii nocase
    $o1 = "off_4BAD9C" wide ascii nocase
    $o2 = "start_8" wide ascii nocase
    $o3 = "_wwincmdln" wide ascii nocase
  condition:
    4 of ($o*)
}