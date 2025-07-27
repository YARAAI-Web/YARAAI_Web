rule auto_rule_20250726105538_5040 {
  strings:
    $o0 = "_CrtIsValidHeapPointer" wide ascii nocase
    $o1 = "flProtect" wide ascii nocase
  condition:
    all of them
}