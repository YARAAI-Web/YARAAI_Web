rule auto_rule_20250726235509_2653 {
  strings:
    $o0 = "TrailUp0_0" wide ascii nocase
    $o1 = "atol" wide ascii nocase
    $o2 = "Program" wide ascii nocase
    $o3 = "algn_45D032" wide ascii nocase
  condition:
    4 of ($o*)
}