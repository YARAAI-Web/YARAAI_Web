rule auto_rule_20250726234313_5488 {
  strings:
    $o0 = "bInitialState" wide ascii nocase
    $o1 = "DdeConnectList" wide ascii nocase
  condition:
    all of them
}