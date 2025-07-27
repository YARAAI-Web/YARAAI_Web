rule auto_rule_20250727041923_6051 {
  strings:
    $o0 = "lpszVolumeMountPoint" wide ascii nocase
    $o1 = "nIDListBox" wide ascii nocase
    $o2 = "lpDevice" wide ascii nocase
    $o3 = "lpWndClass" wide ascii nocase
    $o4 = "GetBinaryType" wide ascii nocase
  condition:
    4 of ($o*)
}