rule auto_rule_20250726224326_2949 {
  strings:
    $o0 = "tionAndSpinCount" wide ascii nocase
    $o1 = "FontFamilyFromName" wide ascii nocase
    $o2 = "aCouldNotLockDi" wide ascii nocase
    $o3 = "_cfltcvt" wide ascii nocase
  condition:
    4 of ($o*)
}