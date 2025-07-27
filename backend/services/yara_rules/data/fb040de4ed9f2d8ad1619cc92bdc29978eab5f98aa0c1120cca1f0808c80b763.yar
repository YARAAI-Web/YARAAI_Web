rule auto_rule_20250727011623_0486 {
  strings:
    $o0 = "cchItemText" wide ascii nocase
    $o1 = "bErase" wide ascii nocase
    $o2 = "DialogBoxIndirectParamA" wide ascii nocase
    $o3 = "DdeSetQualityOfService" wide ascii nocase
  condition:
    4 of ($o*)
}