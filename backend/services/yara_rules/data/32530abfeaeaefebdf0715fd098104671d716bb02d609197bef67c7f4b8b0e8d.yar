rule auto_rule_20250726231712_6622 {
  strings:
    $o0 = "x24F2200" wide ascii nocase
  condition:
    all of them
}