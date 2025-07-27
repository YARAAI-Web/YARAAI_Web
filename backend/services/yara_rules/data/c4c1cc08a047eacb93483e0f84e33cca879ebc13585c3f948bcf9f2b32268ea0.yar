rule auto_rule_20250726074415_5280 {
  strings:
    $o0 = "retfw" wide ascii nocase
    $o1 = "GetMouseMovePointsEx" wide ascii nocase
    $o2 = "cchLength" wide ascii nocase
    $o3 = "hAccelSrc" wide ascii nocase
  condition:
    4 of ($o*)
}