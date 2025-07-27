rule auto_rule_20250726133300_1025 {
  strings:
    $o0 = "EnumPropsA" wide ascii nocase
    $o1 = "LoadKeyboardLayoutA" wide ascii nocase
    $o2 = "wCmd" wide ascii nocase
    $o3 = "IsCharAlphaNumericW" wide ascii nocase
    $o4 = "InSendMessageEx" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726133303_9459 {
  strings:
    $o0 = "uIDHiliteItem" wide ascii nocase
    $o1 = "DdeConnectList" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726133307_8727 {
  condition:
    auto_rule_20250726133300_1025 or auto_rule_20250726133303_9459
}