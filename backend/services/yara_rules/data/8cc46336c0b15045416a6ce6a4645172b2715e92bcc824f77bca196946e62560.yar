rule auto_rule_20250726080106_9988 {
  strings:
    $o0 = "xFFCDBD23" wide ascii nocase
    $o1 = "x613Eu" wide ascii nocase
  condition:
    all of them
}