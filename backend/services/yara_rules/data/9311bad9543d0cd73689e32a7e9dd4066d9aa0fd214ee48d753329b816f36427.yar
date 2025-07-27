rule auto_rule_20250726212354_7132 {
  strings:
    $o0 = "_fptrap" wide ascii nocase
    $o1 = "_CrtIsValidHeapPointer" wide ascii nocase
  condition:
    all of them
}