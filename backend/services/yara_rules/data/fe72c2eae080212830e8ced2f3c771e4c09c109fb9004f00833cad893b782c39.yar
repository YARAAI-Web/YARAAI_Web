rule auto_rule_20250727033922_1043 {
  strings:
    $o0 = "ToUnicode" wide ascii nocase
    $o1 = "hUSKey" wide ascii nocase
    $o2 = "wRemoveMsg" wide ascii nocase
    $o3 = "StrRChrA" wide ascii nocase
    $o4 = "hWinPosInfo" wide ascii nocase
  condition:
    4 of ($o*)
}