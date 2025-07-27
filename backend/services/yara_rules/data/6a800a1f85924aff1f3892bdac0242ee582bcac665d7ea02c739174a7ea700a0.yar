rule auto_rule_20250726182035_6642 {
  strings:
    $o0 = "dword_466AD4" wide ascii nocase
    $o1 = "start_byte_3" wide ascii nocase
    $o2 = "dwInfoType" wide ascii nocase
    $o3 = "_byte_0" wide ascii nocase
    $o4 = "dword_467154" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726182038_9819 {
  strings:
    $o0 = "__sbh_verify_block" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726182042_3566 {
  condition:
    auto_rule_20250726182035_6642 or auto_rule_20250726182038_9819
}