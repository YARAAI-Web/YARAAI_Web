rule auto_rule_20250726163223_4488 {
  strings:
    $o0 = "GetMouseMovePointsEx" wide ascii nocase
  condition:
    all of them
}