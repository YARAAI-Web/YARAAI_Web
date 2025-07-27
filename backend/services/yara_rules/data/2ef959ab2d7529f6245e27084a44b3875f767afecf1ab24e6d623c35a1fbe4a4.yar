rule auto_rule_20250726190421_2207 {
  strings:
    $o0 = "_SEH_epilog" wide ascii nocase
    $o1 = "UnwindUp0_0" wide ascii nocase
    $o2 = "dword_418018" wide ascii nocase
  condition:
    3 of ($o*)
}