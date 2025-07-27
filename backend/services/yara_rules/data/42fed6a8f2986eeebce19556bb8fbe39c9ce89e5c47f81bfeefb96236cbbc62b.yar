rule auto_rule_20250726203732_0107 {
  strings:
    $o0 = "rtcTypeName" wide ascii nocase
    $o1 = "dword_401390" wide ascii nocase
  condition:
    all of them
}