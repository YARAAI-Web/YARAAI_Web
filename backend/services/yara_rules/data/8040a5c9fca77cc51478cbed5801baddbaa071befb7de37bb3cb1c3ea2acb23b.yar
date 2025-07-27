rule auto_rule_20250726191425_3419 {
  strings:
    $o0 = "PathGetArgsA" wide ascii nocase
    $o1 = "hWndChild" wide ascii nocase
    $o2 = "GetNextDlgTabItem" wide ascii nocase
    $o3 = "pblend" wide ascii nocase
  condition:
    4 of ($o*)
}