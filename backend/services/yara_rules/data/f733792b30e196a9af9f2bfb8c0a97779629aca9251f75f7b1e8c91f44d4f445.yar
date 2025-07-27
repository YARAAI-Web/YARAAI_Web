rule auto_rule_20250726090814_7504 {
  strings:
    $o0 = "x3EDDu" wide ascii nocase
  condition:
    all of them
}