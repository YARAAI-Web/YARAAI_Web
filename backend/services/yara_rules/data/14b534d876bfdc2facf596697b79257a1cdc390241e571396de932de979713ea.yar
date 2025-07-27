rule auto_rule_20250726074010_4636 {
  strings:
    $o0 = "GetComboBoxInfo" wide ascii nocase
    $o1 = "DlgDirListComboBoxA" wide ascii nocase
    $o2 = "pcbi" wide ascii nocase
  condition:
    3 of ($o*)
}