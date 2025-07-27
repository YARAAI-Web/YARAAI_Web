rule auto_rule_20250726202607_0267 {
  strings:
    $o0 = "x43135885u" wide ascii nocase
    $o1 = "x67FF3EA3" wide ascii nocase
  condition:
    all of them
}