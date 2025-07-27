rule auto_rule_20250726062151_6669 {
  strings:
    $o0 = "copy_tail_loop" wide ascii nocase
    $o1 = "byte_40F994" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
    $o3 = "dword_411D9C" wide ascii nocase
    $o4 = "dword_41223C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726062154_3119 {
  strings:
    $o0 = "dword_412240" wide ascii nocase
    $o1 = "dword_411EC8" wide ascii nocase
    $o2 = "__sbh_heap_init" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726062200_9674 {
  condition:
    auto_rule_20250726062151_6669 or auto_rule_20250726062154_3119
}