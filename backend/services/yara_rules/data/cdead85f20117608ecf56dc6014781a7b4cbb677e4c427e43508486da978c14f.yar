rule auto_rule_20250726122720_0724 {
  strings:
    $o0 = "bInitialState" wide ascii nocase
    $o1 = "dwAdditionalFlags" wide ascii nocase
    $o2 = "bDisablePriorityBoost" wide ascii nocase
    $o3 = "lpszCurrent" wide ascii nocase
    $o4 = "th32HeapID" wide ascii nocase
  condition:
    4 of ($o*)
}