rule auto_rule_20250726213721_8635 {
  strings:
    $o0 = "pwszKLID" wide ascii nocase
    $o1 = "DefDlgProcA" wide ascii nocase
    $o2 = "SetClipboardData" wide ascii nocase
  condition:
    3 of ($o*)
}