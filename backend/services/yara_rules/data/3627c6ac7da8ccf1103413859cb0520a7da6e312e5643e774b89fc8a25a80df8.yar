rule auto_rule_20250726070237_5442 {
  strings:
    $o0 = "GetForegroundWindow" wide ascii nocase
    $o1 = "hWndNewParent" wide ascii nocase
    $o2 = "pSIRequested" wide ascii nocase
  condition:
    3 of ($o*)
}