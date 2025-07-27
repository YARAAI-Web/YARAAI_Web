rule auto_rule_20250726231513_9155 {
  strings:
    $o0 = "xFFFFFF80" wide ascii nocase
    $o1 = "x400FF" wide ascii nocase
  condition:
    all of them
}