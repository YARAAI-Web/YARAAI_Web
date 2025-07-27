rule auto_rule_20250726191047_8369 {
  strings:
    $o0 = "LocalSize" wide ascii nocase
    $o1 = "lstrlenA" wide ascii nocase
    $o2 = "FreeConsole" wide ascii nocase
    $o3 = "FindVolumeClose" wide ascii nocase
  condition:
    4 of ($o*)
}