rule auto_rule_20250726150356_6471 {
  strings:
    $o0 = "RegisterDeviceNotificationW" wide ascii nocase
    $o1 = "hwndDlg" wide ascii nocase
    $o2 = "EnableMenuItem" wide ascii nocase
  condition:
    3 of ($o*)
}