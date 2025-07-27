rule auto_rule_20250726090002_4847 {
  strings:
    $o0 = "_heap_alloc" wide ascii nocase
    $o1 = "dword_40CF90" wide ascii nocase
    $o2 = "dword_40CDF4" wide ascii nocase
    $o3 = "_ShrMan" wide ascii nocase
  condition:
    4 of ($o*)
}