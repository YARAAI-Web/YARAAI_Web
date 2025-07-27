rule auto_rule_20250726183652_2650 {
  strings:
    $o0 = "hUser" wide ascii nocase
    $o1 = "GetForegroundWindow" wide ascii nocase
    $o2 = "PathUnquoteSpacesA" wide ascii nocase
  condition:
    3 of ($o*)
}