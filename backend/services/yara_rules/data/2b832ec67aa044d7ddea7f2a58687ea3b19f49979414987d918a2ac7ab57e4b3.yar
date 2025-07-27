rule auto_rule_20250726072802_3388 {
  strings:
    $o0 = "WaitHandle" wide ascii nocase
    $o1 = "hcur" wide ascii nocase
    $o2 = "DdeConnectList" wide ascii nocase
  condition:
    3 of ($o*)
}