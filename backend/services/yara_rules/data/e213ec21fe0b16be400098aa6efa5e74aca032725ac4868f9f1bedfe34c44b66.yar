rule auto_rule_20250727040859_5919 {
  strings:
    $o0 = "word_4335F0" wide ascii nocase
    $o1 = "byte_4336C6" wide ascii nocase
  condition:
    all of them
}