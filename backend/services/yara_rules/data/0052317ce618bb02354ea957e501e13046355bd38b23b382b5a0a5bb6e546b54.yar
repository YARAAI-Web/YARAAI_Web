rule auto_rule_20250726124607_3621 {
  strings:
    $o0 = "lpsi" wide ascii nocase
    $o1 = "lpParameterBlock" wide ascii nocase
  condition:
    all of them
}