rule auto_rule_20250726110234_4813 {
  strings:
    $o0 = "FreeDDElParam" wide ascii nocase
    $o1 = "CloseWindow" wide ascii nocase
    $o2 = "lpszWinSta" wide ascii nocase
  condition:
    3 of ($o*)
}