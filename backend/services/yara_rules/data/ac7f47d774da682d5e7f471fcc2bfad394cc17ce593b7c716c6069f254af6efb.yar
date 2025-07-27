rule auto_rule_20250726093513_8196 {
  strings:
    $o0 = "runtime__ptr_gcCPULimiterState_finishGCTransition" wide ascii nocase
    $o1 = "chansend1" wide ascii nocase
    $o2 = "runtime__ptr_mcentral_cacheSpan" wide ascii nocase
    $o3 = "runtime_notetsleep_internal" wide ascii nocase
  condition:
    4 of ($o*)
}