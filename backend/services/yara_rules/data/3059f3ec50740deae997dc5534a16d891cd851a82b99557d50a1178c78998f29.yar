rule auto_rule_20250726080245_4786 {
  strings:
    $o0 = "x17000u" wide ascii nocase
    $o1 = "GetStockObject" wide ascii nocase
  condition:
    all of them
}