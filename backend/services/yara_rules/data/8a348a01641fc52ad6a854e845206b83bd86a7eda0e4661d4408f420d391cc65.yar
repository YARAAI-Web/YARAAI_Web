rule auto_rule_20250726101534_0672 {
  strings:
    $o0 = "tMIXERCONTROLDETAILS" wide ascii nocase
    $o1 = "byte_411640" wide ascii nocase
    $o2 = "_heap_alloc" wide ascii nocase
    $o3 = "doexit" wide ascii nocase
    $o4 = "dword_411984" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726101537_7368 {
  strings:
    $o0 = "dword_411D40" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726101540_6482 {
  condition:
    auto_rule_20250726101534_0672 or auto_rule_20250726101537_7368
}