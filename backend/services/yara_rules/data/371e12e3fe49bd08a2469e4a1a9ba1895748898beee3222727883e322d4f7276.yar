rule auto_rule_20250726222149_5412 {
  strings:
    $o0 = "prcScroll" wide ascii nocase
    $o1 = "lstrcatA" wide ascii nocase
    $o2 = "RegOpenKeyA" wide ascii nocase
    $o3 = "lpMenuName" wide ascii nocase
    $o4 = "hData" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726222153_5320 {
  strings:
    $o0 = "DdeReconnect" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726222158_9038 {
  condition:
    auto_rule_20250726222149_5412 or auto_rule_20250726222153_5320
}