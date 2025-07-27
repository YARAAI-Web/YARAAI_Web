rule auto_rule_20250726232009_5463 {
  strings:
    $o0 = "IMPGetIMEA" wide ascii nocase
    $o1 = "GetGUIThreadInfo" wide ascii nocase
    $o2 = "DdeQueryStringW" wide ascii nocase
    $o3 = "GlobalAddAtomW" wide ascii nocase
  condition:
    4 of ($o*)
}