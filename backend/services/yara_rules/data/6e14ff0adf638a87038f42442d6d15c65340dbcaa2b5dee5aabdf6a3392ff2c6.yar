rule auto_rule_20250726182813_7523 {
  strings:
    $o0 = "DdeImpersonateClient" wide ascii nocase
    $o1 = "lpFiber" wide ascii nocase
    $o2 = "pInputControl" wide ascii nocase
    $o3 = "lpProgressRoutine" wide ascii nocase
  condition:
    4 of ($o*)
}