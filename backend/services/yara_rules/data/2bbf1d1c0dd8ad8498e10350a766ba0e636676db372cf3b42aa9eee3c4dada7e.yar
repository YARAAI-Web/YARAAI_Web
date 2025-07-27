rule auto_rule_20250726171826_8464 {
  strings:
    $o0 = "debug" wide ascii nocase
    $o1 = "_calloc_dbg" wide ascii nocase
    $o2 = "_CrtIsValidHeapPointer" wide ascii nocase
  condition:
    3 of ($o*)
}