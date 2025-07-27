rule auto_rule_20250726114607_4055 {
  strings:
    $o0 = "MoveFileExA" wide ascii nocase
    $o1 = "ScopeIndex" wide ascii nocase
  condition:
    all of them
}