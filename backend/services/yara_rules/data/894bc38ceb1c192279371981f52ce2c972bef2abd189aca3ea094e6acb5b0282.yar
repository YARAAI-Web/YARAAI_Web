rule auto_rule_20250726100301_5321 {
  strings:
    $o0 = "lpVolumeName" wide ascii nocase
    $o1 = "CreateMailslotW" wide ascii nocase
    $o2 = "GetDlgCtrlID" wide ascii nocase
  condition:
    3 of ($o*)
}