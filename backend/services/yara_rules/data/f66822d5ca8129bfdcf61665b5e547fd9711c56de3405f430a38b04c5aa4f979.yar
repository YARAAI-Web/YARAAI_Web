rule auto_rule_20250726210422_6755 {
  strings:
    $o0 = "lpReadTimeout" wide ascii nocase
    $o1 = "dwFreq" wide ascii nocase
    $o2 = "lpNumberOfFreeClusters" wide ascii nocase
    $o3 = "IsDialogMessageW" wide ascii nocase
    $o4 = "WritePrivateProfileSectionW" wide ascii nocase
  condition:
    4 of ($o*)
}