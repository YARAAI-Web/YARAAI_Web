rule auto_rule_20250726204949_3110 {
  strings:
    $o0 = "pfnFilterProc" wide ascii nocase
    $o1 = "xlat" wide ascii nocase
  condition:
    all of them
}