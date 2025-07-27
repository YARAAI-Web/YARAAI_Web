rule auto_rule_20250726234029_4280 {
  strings:
    $o0 = "gowrap2" wide ascii nocase
    $o1 = "runtime__ptr_mspan_initHeapBits" wide ascii nocase
  condition:
    all of them
}