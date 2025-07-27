rule auto_rule_20250726203515_1300 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "dword_469D40" wide ascii nocase
  condition:
    all of them
}