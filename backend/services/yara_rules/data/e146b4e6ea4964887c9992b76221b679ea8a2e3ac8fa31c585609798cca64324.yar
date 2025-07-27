rule auto_rule_20250726084221_0132 {
  strings:
    $o0 = "runtime_Caller" wide ascii nocase
    $o1 = "runtime_gcMarkTermination_forEachP_func6" wide ascii nocase
    $o2 = "internal_bytealg_countGenericString_0" wide ascii nocase
    $o3 = "runtime__ptr_timeHistogram_record" wide ascii nocase
  condition:
    4 of ($o*)
}