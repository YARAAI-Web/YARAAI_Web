rule auto_rule_20250726084342_0803 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "_malloc_dbg" wide ascii nocase
  condition:
    all of them
}