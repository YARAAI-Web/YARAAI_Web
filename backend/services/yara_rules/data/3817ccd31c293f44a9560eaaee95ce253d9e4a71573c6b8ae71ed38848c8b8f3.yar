rule auto_rule_20250726214501_6343 {
  strings:
    $o0 = "SetClassLongW" wide ascii nocase
    $o1 = "lpModemStat" wide ascii nocase
    $o2 = "hkAssoc" wide ascii nocase
    $o3 = "lpResultCallBack" wide ascii nocase
    $o4 = "pszSubkey" wide ascii nocase
  condition:
    4 of ($o*)
}