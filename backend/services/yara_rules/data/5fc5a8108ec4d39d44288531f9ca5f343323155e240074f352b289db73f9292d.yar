rule auto_rule_20250727005542_1487 {
  strings:
    $o0 = "ProcessorFeature" wide ascii nocase
    $o1 = "CreateWaitableTimerW" wide ascii nocase
    $o2 = "fResume" wide ascii nocase
    $o3 = "LoadCursorA" wide ascii nocase
  condition:
    4 of ($o*)
}