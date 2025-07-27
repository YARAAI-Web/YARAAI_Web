rule auto_rule_20250726102204_9874 {
  strings:
    $o0 = "dword_467EBC" wide ascii nocase
    $o1 = "_heap_alloc_base" wide ascii nocase
    $o2 = "dword_468014" wide ascii nocase
  condition:
    3 of ($o*)
}