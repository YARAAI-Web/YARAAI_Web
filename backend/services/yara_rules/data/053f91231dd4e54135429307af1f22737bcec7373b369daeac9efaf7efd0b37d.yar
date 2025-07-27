rule auto_rule_20250727003440_7287 {
  strings:
    $o0 = "FontA" wide ascii nocase
    $o1 = "x1FC0" wide ascii nocase
  condition:
    all of them
}