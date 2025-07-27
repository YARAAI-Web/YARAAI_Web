rule auto_rule_20250726161633_5143 {
  strings:
    $o0 = "dword_411AB8" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
    $o2 = "start_byte_3" wide ascii nocase
    $o3 = "dword_411594" wide ascii nocase
    $o4 = "_heap_init" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726161636_9069 {
  strings:
    $o0 = "tail_loop_start" wide ascii nocase
    $o1 = "dword_4119A8" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726161646_0993 {
  condition:
    auto_rule_20250726161633_5143 or auto_rule_20250726161636_9069
}