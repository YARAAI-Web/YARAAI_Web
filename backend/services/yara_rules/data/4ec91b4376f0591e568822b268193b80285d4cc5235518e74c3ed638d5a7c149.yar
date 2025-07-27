rule auto_rule_20250726080547_1070 {
  strings:
    $o0 = "NotifyWinEvent" wide ascii nocase
    $o1 = "gaFlags" wide ascii nocase
  condition:
    all of them
}