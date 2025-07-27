rule auto_rule_20250726152413_6052 {
  strings:
    $o0 = "hWndChild" wide ascii nocase
    $o1 = "DefDlgProcW" wide ascii nocase
    $o2 = "ChildWindowFromPointEx" wide ascii nocase
    $o3 = "hrgnClip" wide ascii nocase
  condition:
    4 of ($o*)
}