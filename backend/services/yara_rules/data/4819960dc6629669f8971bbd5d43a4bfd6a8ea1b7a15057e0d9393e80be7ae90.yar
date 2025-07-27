rule auto_rule_20250726151321_4088 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "word_454582" wide ascii nocase
  condition:
    all of them
}