rule auto_rule_20250727001555_4724 {
  strings:
    $o0 = "CascadeChildWindows" wide ascii nocase
    $o1 = "IMPQueryIMEW" wide ascii nocase
    $o2 = "GetDoubleClickTime" wide ascii nocase
    $o3 = "DlgDirSelectExW" wide ascii nocase
    $o4 = "dwExStyle" wide ascii nocase
  condition:
    4 of ($o*)
}