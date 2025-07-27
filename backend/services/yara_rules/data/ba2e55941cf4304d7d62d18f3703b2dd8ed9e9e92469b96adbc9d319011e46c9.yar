rule auto_rule_20250727040330_1072 {
  strings:
    $o0 = "nIDDlgItem" wide ascii nocase
    $o1 = "lstrcatW" wide ascii nocase
    $o2 = "TranslateAcceleratorW" wide ascii nocase
    $o3 = "flAllocationType" wide ascii nocase
    $o4 = "lpcbData" wide ascii nocase
  condition:
    5 of ($o*)
}