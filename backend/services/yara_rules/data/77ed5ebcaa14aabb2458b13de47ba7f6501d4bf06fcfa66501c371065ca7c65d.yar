rule auto_rule_20250726191521_9365 {
  strings:
    $o0 = "lpszCurrent" wide ascii nocase
    $o1 = "SetMenuItemInfoA" wide ascii nocase
    $o2 = "DdeNameService" wide ascii nocase
    $o3 = "lpszDesktop" wide ascii nocase
  condition:
    4 of ($o*)
}