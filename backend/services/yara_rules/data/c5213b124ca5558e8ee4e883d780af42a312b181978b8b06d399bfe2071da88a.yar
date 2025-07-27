rule auto_rule_20250726124334_0749 {
  strings:
    $o0 = "off_408548" wide ascii nocase
    $o1 = "x1013u" wide ascii nocase
  condition:
    all of them
}