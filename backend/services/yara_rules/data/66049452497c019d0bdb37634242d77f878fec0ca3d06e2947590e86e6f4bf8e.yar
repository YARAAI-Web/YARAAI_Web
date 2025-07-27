rule auto_rule_20250726213436_4903 {
  strings:
    $o0 = "x4AA00000DB6LL" wide ascii nocase
    $o1 = "off_428393" wide ascii nocase
  condition:
    all of them
}