rule auto_rule_20250726125550_0085 {
  strings:
    $o0 = "x3421" wide ascii nocase
    $o1 = "x78FD" wide ascii nocase
  condition:
    all of them
}