rule auto_rule_20250726162001_8514 {
  strings:
    $o0 = "_heap_alloc_dbg" wide ascii nocase
    $o1 = "dword_467300" wide ascii nocase
    $o2 = "off_46750C" wide ascii nocase
  condition:
    3 of ($o*)
}