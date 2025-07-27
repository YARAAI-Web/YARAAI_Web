rule auto_rule_20250726120705_0519 {
  strings:
    $o0 = "GetTopWindow" wide ascii nocase
    $o1 = "byte_476AE1" wide ascii nocase
    $o2 = "_heap_alloc" wide ascii nocase
  condition:
    3 of ($o*)
}