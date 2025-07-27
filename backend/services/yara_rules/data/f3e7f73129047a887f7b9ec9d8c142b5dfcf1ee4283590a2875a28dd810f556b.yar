rule auto_rule_20250726201145_8026 {
  strings:
    $o0 = "hDialogTemplate" wide ascii nocase
    $o1 = "ReadConsoleOutputW" wide ascii nocase
    $o2 = "lpSecurityAttributes" wide ascii nocase
    $o3 = "GetUpdateRect" wide ascii nocase
  condition:
    4 of ($o*)
}