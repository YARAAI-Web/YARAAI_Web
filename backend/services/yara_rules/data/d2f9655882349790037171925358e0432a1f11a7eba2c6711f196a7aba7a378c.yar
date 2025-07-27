rule auto_rule_20250726085036_6267 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "ualAllocEx" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
    $o3 = "main_loop_entrance_0" wide ascii nocase
  condition:
    4 of ($o*)
}