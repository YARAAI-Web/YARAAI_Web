rule auto_rule_20250726203200_7746 {
  strings:
    $o0 = "pfnCompletionRoutine" wide ascii nocase
    $o1 = "lPeriod" wide ascii nocase
    $o2 = "xF89C85B8" wide ascii nocase
  condition:
    3 of ($o*)
}