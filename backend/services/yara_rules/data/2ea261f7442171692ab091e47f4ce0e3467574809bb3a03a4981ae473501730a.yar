rule auto_rule_20250726201047_4973 {
  strings:
    $o0 = "main_loop_start" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
    $o3 = "start_byte_3" wide ascii nocase
    $o4 = "x18000" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726201050_0172 {
  strings:
    $o0 = "joyGetDevCapsA" wide ascii nocase
    $o1 = "RtlUnwind" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726201100_4351 {
  condition:
    auto_rule_20250726201047_4973 or auto_rule_20250726201050_0172
}