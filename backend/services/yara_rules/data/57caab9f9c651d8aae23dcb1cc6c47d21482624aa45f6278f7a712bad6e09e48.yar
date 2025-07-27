rule auto_rule_20250727032105_6389 {
  strings:
    $o0 = "GetMenuItemRect" wide ascii nocase
    $o1 = "SetClipboardViewer" wide ascii nocase
  condition:
    all of them
}