rule auto_rule_20250726081858_3929 {
  strings:
    $o0 = "_except_handler3" wide ascii nocase
    $o1 = "x140u" wide ascii nocase
    $o2 = "copy_start" wide ascii nocase
    $o3 = "_heap_alloc" wide ascii nocase
    $o4 = "dword_411D68" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726081901_2847 {
  strings:
    $o0 = "x4020D4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726081913_2045 {
  condition:
    auto_rule_20250726081858_3929 or auto_rule_20250726081901_2847
}