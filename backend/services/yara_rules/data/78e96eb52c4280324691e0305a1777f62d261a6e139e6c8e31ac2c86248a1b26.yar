rule auto_rule_20250727014652_7065 {
  strings:
    $o0 = "_heap_alloc_dbg" wide ascii nocase
    $o1 = "allocated" wide ascii nocase
  condition:
    all of them
}