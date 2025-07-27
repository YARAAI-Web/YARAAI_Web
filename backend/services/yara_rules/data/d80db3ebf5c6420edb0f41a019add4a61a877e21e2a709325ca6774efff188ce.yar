rule auto_rule_20250726185512_9469 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "__sbh_heap_init" wide ascii nocase
    $o2 = "dword_440434" wide ascii nocase
    $o3 = "dword_440550" wide ascii nocase
  condition:
    4 of ($o*)
}