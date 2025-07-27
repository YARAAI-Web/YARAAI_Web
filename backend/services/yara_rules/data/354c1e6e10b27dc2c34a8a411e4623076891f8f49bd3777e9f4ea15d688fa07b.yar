rule auto_rule_20250726082442_3993 {
  strings:
    $o0 = "dword_463B08" wide ascii nocase
    $o1 = "_malloc_dbg" wide ascii nocase
  condition:
    all of them
}