rule auto_rule_20250726153843_2451 {
  strings:
    $o0 = "j_RtlUnwind" wide ascii nocase
    $o1 = "word_40C5A0" wide ascii nocase
  condition:
    all of them
}