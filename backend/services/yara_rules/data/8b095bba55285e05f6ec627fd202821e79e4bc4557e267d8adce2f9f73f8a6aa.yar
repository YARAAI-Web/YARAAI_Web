rule auto_rule_20250727004259_2205 {
  strings:
    $o0 = "runtime_notetsleepg" wide ascii nocase
    $o1 = "runtime__ptr_scavengeIndex_find" wide ascii nocase
    $o2 = "refill" wide ascii nocase
    $o3 = "runtime_stkbucket" wide ascii nocase
    $o4 = "runtime_greyobject" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727004300_0486 {
  strings:
    $o0 = "runtime_debugCallWrap2_func1" wide ascii nocase
    $o1 = "memequal8" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727004311_6528 {
  condition:
    auto_rule_20250727004259_2205 or auto_rule_20250727004300_0486
}