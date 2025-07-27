rule auto_rule_20250726195416_0108 {
  strings:
    $o0 = "BFBh" wide ascii nocase
    $o1 = "YAmount" wide ascii nocase
    $o2 = "nFilterType" wide ascii nocase
    $o3 = "pmbi" wide ascii nocase
  condition:
    4 of ($o*)
}