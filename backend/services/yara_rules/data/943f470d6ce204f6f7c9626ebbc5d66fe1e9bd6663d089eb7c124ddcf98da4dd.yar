rule auto_rule_20250726153638_9267 {
  strings:
    $o0 = "lpEventTrack" wide ascii nocase
    $o1 = "OemKeyScan" wide ascii nocase
    $o2 = "nIDDlgItem" wide ascii nocase
  condition:
    3 of ($o*)
}