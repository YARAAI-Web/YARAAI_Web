rule auto_rule_20250726173338_1702 {
  strings:
    $o0 = "dwInitParam" wide ascii nocase
    $o1 = "xCC3DD42F" wide ascii nocase
    $o2 = "lpCharType" wide ascii nocase
    $o3 = "dwTable" wide ascii nocase
    $o4 = "lpDistanceToMoveHigh" wide ascii nocase
  condition:
    4 of ($o*)
}