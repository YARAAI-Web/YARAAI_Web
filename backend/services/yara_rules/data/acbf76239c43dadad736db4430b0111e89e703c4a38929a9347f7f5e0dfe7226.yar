rule auto_rule_20250726223745_3361 {
  strings:
    $o0 = "dword_412224" wide ascii nocase
    $o1 = "dword_411DA0" wide ascii nocase
    $o2 = "_heap_alloc" wide ascii nocase
    $o3 = "dword_411D50" wide ascii nocase
    $o4 = "x5000u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726223748_0598 {
  strings:
    $o0 = "byte_412001" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726223753_1832 {
  condition:
    auto_rule_20250726223745_3361 or auto_rule_20250726223748_0598
}