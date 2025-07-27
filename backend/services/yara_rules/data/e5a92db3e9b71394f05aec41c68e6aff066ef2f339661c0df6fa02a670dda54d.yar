rule auto_rule_20250726091736_8850 {
  strings:
    $o0 = "off_42E435" wide ascii nocase
    $o1 = "x3273u" wide ascii nocase
  condition:
    all of them
}