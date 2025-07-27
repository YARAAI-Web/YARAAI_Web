rule auto_rule_20250726141310_6965 {
  strings:
    $o0 = "fInfoLevelId" wide ascii nocase
    $o1 = "nAtom" wide ascii nocase
    $o2 = "lpPath" wide ascii nocase
  condition:
    3 of ($o*)
}