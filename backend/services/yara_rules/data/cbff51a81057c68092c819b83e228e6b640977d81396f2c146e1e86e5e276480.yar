rule auto_rule_20250726145909_3308 {
  strings:
    $o0 = "DdeUnaccessData" wide ascii nocase
    $o1 = "pSID" wide ascii nocase
  condition:
    all of them
}