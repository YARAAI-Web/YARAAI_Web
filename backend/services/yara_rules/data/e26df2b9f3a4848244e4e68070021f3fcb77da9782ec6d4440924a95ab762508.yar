rule auto_rule_20250726170413_1752 {
  strings:
    $o0 = "vKey" wide ascii nocase
    $o1 = "lpIconName" wide ascii nocase
    $o2 = "uFormat" wide ascii nocase
    $o3 = "pSIRequested" wide ascii nocase
    $o4 = "ReplyMessage" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726170416_4166 {
  strings:
    $o0 = "CallMsgFilter" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726170419_0828 {
  condition:
    auto_rule_20250726170413_1752 or auto_rule_20250726170416_4166
}