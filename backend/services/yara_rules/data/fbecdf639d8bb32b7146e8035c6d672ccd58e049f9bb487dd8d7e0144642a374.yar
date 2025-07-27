rule auto_rule_20250727021646_7576 {
  strings:
    $o0 = "InternalGetWindowText" wide ascii nocase
    $o1 = "CreateDesktopW" wide ascii nocase
    $o2 = "x17000u" wide ascii nocase
    $o3 = "grfFlags" wide ascii nocase
    $o4 = "IsCharLowerA" wide ascii nocase
  condition:
    4 of ($o*)
}