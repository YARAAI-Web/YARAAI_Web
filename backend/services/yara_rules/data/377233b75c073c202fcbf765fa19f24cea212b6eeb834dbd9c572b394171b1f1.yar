rule auto_rule_20250726202627_1397 {
  strings:
    $o0 = "ExcludeUpdateRgn" wide ascii nocase
    $o1 = "lpDisplayDevice" wide ascii nocase
    $o2 = "aS1ftware" wide ascii nocase
    $o3 = "hDesktop" wide ascii nocase
    $o4 = "DdeConnectList" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726202631_8582 {
  strings:
    $o0 = "aClassesClsid08" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726202634_7508 {
  condition:
    auto_rule_20250726202627_1397 or auto_rule_20250726202631_8582
}