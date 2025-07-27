rule auto_rule_20250726182740_0389 {
  strings:
    $o0 = "dword_40B000" wide ascii nocase
    $o1 = "__sbh_heap_init" wide ascii nocase
    $o2 = "dword_449EE8" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
    $o4 = "dwInfoType" wide ascii nocase
  condition:
    4 of ($o*)
}