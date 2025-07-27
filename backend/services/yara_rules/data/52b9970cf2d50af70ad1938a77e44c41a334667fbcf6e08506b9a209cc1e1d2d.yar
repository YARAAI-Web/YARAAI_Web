rule auto_rule_20250726185316_5410 {
  strings:
    $o0 = "_heap_alloc" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "UnwindUp4_0" wide ascii nocase
    $o3 = "stru_406060" wide ascii nocase
  condition:
    4 of ($o*)
}