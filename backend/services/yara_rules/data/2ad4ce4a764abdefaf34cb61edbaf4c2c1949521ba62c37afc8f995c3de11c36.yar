rule auto_rule_20250726221921_1522 {
  strings:
    $o0 = "uFormat" wide ascii nocase
    $o1 = "lpptBuf" wide ascii nocase
    $o2 = "SwapMouseButton" wide ascii nocase
    $o3 = "cchLength" wide ascii nocase
    $o4 = "dword_41A708" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726221924_7672 {
  strings:
    $o0 = "hszTopic" wide ascii nocase
    $o1 = "idComboBox" wide ascii nocase
    $o2 = "hwndFrom" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726221928_7239 {
  condition:
    auto_rule_20250726221921_1522 or auto_rule_20250726221924_7672
}