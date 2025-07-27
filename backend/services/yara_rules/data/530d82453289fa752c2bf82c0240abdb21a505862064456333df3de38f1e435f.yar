rule auto_rule_20250726152829_7619 {
  strings:
    $o0 = "MoveFileWithProgressA" wide ascii nocase
  condition:
    all of them
}