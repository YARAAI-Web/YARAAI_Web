rule auto_rule_20250726081600_5446 {
  strings:
    $o0 = "runtime_recvDirect" wide ascii nocase
    $o1 = "scavengeIndex" wide ascii nocase
    $o2 = "runtime__ptr_mspan_countAlloc" wide ascii nocase
    $o3 = "resetLive" wide ascii nocase
    $o4 = "finalizercommit" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726081603_9042 {
  strings:
    $o0 = "internal_chacha8rand_block" wide ascii nocase
    $o1 = "runtime_convTnoptr" wide ascii nocase
    $o2 = "fram" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726081606_8785 {
  condition:
    auto_rule_20250726081600_5446 or auto_rule_20250726081603_9042
}