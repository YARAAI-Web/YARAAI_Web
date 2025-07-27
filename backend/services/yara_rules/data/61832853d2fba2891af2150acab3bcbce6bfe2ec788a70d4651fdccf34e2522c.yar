rule auto_rule_20250727004856_5963 {
  strings:
    $o0 = "x1C44CDB80DDE85E3LL" wide ascii nocase
  condition:
    all of them
}