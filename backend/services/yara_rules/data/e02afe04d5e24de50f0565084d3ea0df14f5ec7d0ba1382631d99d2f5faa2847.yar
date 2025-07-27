rule auto_rule_20250727010427_2699 {
  strings:
    $o0 = "word_42E222" wide ascii nocase
    $o1 = "x480u" wide ascii nocase
    $o2 = "x4155A0" wide ascii nocase
  condition:
    3 of ($o*)
}