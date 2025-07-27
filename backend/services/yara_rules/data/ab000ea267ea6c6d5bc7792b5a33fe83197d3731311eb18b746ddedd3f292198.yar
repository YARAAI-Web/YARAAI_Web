rule auto_rule_20250727005529_5989 {
  strings:
    $o0 = "lpProgressRoutine" wide ascii nocase
    $o1 = "LocalCompact" wide ascii nocase
  condition:
    all of them
}