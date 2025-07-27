rule auto_rule_20250727000209_7650 {
  strings:
    $o0 = "hwndDlg" wide ascii nocase
    $o1 = "lpTapeInformation" wide ascii nocase
    $o2 = "PageSetupDlgW" wide ascii nocase
  condition:
    3 of ($o*)
}