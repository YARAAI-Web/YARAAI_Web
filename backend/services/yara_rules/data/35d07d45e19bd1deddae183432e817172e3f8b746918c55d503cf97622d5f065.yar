rule auto_rule_20250726224810_1609 {
  strings:
    $o0 = "__sbh_heap_init" wide ascii nocase
    $o1 = "dword_45DB00" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
  condition:
    3 of ($o*)
}