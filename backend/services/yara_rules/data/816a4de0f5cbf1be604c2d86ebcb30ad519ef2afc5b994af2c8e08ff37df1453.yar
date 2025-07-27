rule auto_rule_20250726144636_3792 {
  strings:
    $o0 = "RegisterDeviceNotificationW" wide ascii nocase
    $o1 = "hNamedPipe" wide ascii nocase
    $o2 = "DdeQueryStringA" wide ascii nocase
  condition:
    3 of ($o*)
}