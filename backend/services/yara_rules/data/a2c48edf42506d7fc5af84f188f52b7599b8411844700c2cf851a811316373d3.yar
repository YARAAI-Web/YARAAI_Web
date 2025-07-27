rule auto_rule_20250727010911_7656 {
  strings:
    $o0 = "RedrawWindow" wide ascii nocase
    $o1 = "AllocConsole" wide ascii nocase
    $o2 = "ProcessorFeature" wide ascii nocase
    $o3 = "SetConsoleCtrlHandler" wide ascii nocase
  condition:
    4 of ($o*)
}