rule auto_rule_20250726171736_4839 {
  strings:
    $o0 = "xmmword_180044E94" wide ascii nocase
    $o1 = "xmmword_1800455C2" wide ascii nocase
  condition:
    all of them
}