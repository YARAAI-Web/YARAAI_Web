rule auto_rule_20250726235602_0388 {
  strings:
    $o0 = "DdeConnect" wide ascii nocase
    $o1 = "SetProcessShutdownParameters" wide ascii nocase
    $o2 = "nIDButton" wide ascii nocase
    $o3 = "lpNumberOfEventsWritten" wide ascii nocase
    $o4 = "lpSecurityAttributes" wide ascii nocase
  condition:
    4 of ($o*)
}