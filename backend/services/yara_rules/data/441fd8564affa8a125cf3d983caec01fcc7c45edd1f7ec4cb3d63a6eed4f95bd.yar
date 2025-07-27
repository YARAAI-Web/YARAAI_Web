rule auto_rule_20250726111212_0829 {
  strings:
    $o0 = "GetProcessPriorityBoost" wide ascii nocase
    $o1 = "MapDialogRect" wide ascii nocase
  condition:
    all of them
}