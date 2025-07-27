rule auto_rule_20250726090548_6992 {
  strings:
    $o0 = "_calloc_dbg" wide ascii nocase
  condition:
    all of them
}