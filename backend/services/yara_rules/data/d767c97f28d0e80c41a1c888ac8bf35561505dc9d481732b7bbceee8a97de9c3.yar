rule auto_rule_20250726092409_1862 {
  strings:
    $o0 = "_cinit" wide ascii nocase
    $o1 = "dword_469CE4" wide ascii nocase
  condition:
    all of them
}