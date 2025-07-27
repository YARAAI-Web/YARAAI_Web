rule auto_rule_20250727003204_3276 {
  strings:
    $o0 = "_ptr_abi_Type" wide ascii nocase
    $o1 = "stdcall0" wide ascii nocase
    $o2 = "runtime__ptr_atomicOffAddr_StoreMin" wide ascii nocase
    $o3 = "runtime_readRandom" wide ascii nocase
    $o4 = "And8" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727003207_6152 {
  strings:
    $o0 = "internal_runtime_atomic_CasRel" wide ascii nocase
    $o1 = "runtime_putempty" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727003211_7541 {
  condition:
    auto_rule_20250727003204_3276 or auto_rule_20250727003207_6152
}