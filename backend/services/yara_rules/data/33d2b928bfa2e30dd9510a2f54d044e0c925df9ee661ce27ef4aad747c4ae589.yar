rule auto_rule_20250726223336_0510 {
  strings:
    $o0 = "chCount" wide ascii nocase
    $o1 = "lpNumberOfEventsRead" wide ascii nocase
    $o2 = "cbMax" wide ascii nocase
    $o3 = "InSendMessageEx" wide ascii nocase
  condition:
    4 of ($o*)
}