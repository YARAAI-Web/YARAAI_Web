rule auto_rule_20250726141911_0999 {
  strings:
    $o0 = "DdeAccessData" wide ascii nocase
    $o1 = "bSigned" wide ascii nocase
    $o2 = "lpszWinSta" wide ascii nocase
  condition:
    3 of ($o*)
}