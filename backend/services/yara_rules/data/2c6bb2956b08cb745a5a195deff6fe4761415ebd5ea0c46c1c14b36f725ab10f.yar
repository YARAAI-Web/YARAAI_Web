rule auto_rule_20250727014943_0537 {
  strings:
    $o0 = "GetSubMenu" wide ascii nocase
    $o1 = "CascadeChildWindows" wide ascii nocase
    $o2 = "GetUserObjectSecurity" wide ascii nocase
    $o3 = "GetClassNameA" wide ascii nocase
    $o4 = "hWndNewViewer" wide ascii nocase
  condition:
    4 of ($o*)
}