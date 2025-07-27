rule auto_rule_20250726221152_5298 {
  strings:
    $o0 = "x140CC94DBLL" wide ascii nocase
  condition:
    all of them
}