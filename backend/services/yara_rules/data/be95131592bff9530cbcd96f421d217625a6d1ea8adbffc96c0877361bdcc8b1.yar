rule auto_rule_20250726141204_5629 {
  strings:
    $o0 = "CharNextA" wide ascii nocase
    $o1 = "GetSysColorBrush" wide ascii nocase
    $o2 = "pszItemText" wide ascii nocase
    $o3 = "DdeCreateStringHandleA" wide ascii nocase
    $o4 = "DdeUnaccessData" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726141207_1975 {
  strings:
    $o0 = "LoadMenuIndirectW" wide ascii nocase
    $o1 = "CloseWindow" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726141211_6118 {
  condition:
    auto_rule_20250726141204_5629 or auto_rule_20250726141207_1975
}