rule auto_rule_20250726101639_2449 {
  strings:
    $o0 = "tionAndSpinCount" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_45C1C8" wide ascii nocase
    $o3 = "_SEH_epilog" wide ascii nocase
  condition:
    4 of ($o*)
}