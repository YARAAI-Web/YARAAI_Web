rule auto_rule_20250726162747_5614 {
  strings:
    $o0 = "redraw" wide ascii nocase
    $o1 = "hWndClient" wide ascii nocase
    $o2 = "GetMenuItemInfoW" wide ascii nocase
    $o3 = "uiParam" wide ascii nocase
    $o4 = "GetOpenClipboardWindow" wide ascii nocase
  condition:
    5 of ($o*)
}