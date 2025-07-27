rule auto_rule_20250726201008_6753 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "dword_4587E8" wide ascii nocase
    $o2 = "_SEH_epilog" wide ascii nocase
  condition:
    3 of ($o*)
}