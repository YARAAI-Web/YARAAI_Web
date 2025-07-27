rule auto_rule_20250726093654_1582 {
  strings:
    $o0 = "CallNextHookEx" wide ascii nocase
    $o1 = "GetPropA" wide ascii nocase
    $o2 = "LockWorkStation" wide ascii nocase
    $o3 = "CreateWindowStationA" wide ascii nocase
  condition:
    4 of ($o*)
}