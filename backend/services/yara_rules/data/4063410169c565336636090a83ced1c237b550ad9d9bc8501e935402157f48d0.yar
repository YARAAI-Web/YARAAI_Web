rule auto_rule_20250726153133_4269 {
  strings:
    $o0 = "BackupRead" wide ascii nocase
    $o1 = "SetConsoleCtrlHandler" wide ascii nocase
    $o2 = "EraseTape" wide ascii nocase
    $o3 = "GetDialogBaseUnits" wide ascii nocase
    $o4 = "lpszVolumeMountPoint" wide ascii nocase
  condition:
    4 of ($o*)
}