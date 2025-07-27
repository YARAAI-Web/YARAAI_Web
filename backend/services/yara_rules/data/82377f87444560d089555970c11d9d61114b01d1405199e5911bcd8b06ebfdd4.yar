rule auto_rule_20250726160438_4346 {
  strings:
    $o0 = "ProcessIdToSessionId" wide ascii nocase
    $o1 = "lread" wide ascii nocase
    $o2 = "flAllocationType" wide ascii nocase
  condition:
    3 of ($o*)
}