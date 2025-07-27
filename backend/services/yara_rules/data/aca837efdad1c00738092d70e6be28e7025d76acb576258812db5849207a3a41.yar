rule auto_rule_20250726134129_4139 {
  strings:
    $o0 = "GetNextDlgTabItem" wide ascii nocase
    $o1 = "FlushInstructionCache" wide ascii nocase
    $o2 = "GetStockObject" wide ascii nocase
    $o3 = "nMaxUserNameSize" wide ascii nocase
    $o4 = "hConsoleInput" wide ascii nocase
  condition:
    4 of ($o*)
}