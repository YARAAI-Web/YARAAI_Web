rule auto_rule_20250726142734_5063 {
  strings:
    $o0 = "xC0000093" wide ascii nocase
    $o1 = "_pLastBlock" wide ascii nocase
  condition:
    all of them
}