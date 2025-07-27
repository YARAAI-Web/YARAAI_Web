rule auto_rule_20250726191713_1744 {
  strings:
    $o0 = "_seh_filter_dll" wide ascii nocase
    $o1 = "LDQi0M8t314" wide ascii nocase
    $o2 = "__scrt_dllmain_crt_thread_attach" wide ascii nocase
    $o3 = "KXQCSKHPNLcw3Mhr" wide ascii nocase
  condition:
    4 of ($o*)
}