rule auto_rule_20250726212746_7434 {
  strings:
    $o0 = "HeapWalk" wide ascii nocase
    $o1 = "lpszFileName" wide ascii nocase
    $o2 = "lpTimerName" wide ascii nocase
  condition:
    3 of ($o*)
}