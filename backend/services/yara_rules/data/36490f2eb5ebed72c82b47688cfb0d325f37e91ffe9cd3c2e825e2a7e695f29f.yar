rule auto_rule_20250726093738_2504 {
  strings:
    $o0 = "SendMessageCallbackW" wide ascii nocase
    $o1 = "TileChildWindows" wide ascii nocase
    $o2 = "InternalGetWindowText" wide ascii nocase
    $o3 = "RegisterShellHookWindow" wide ascii nocase
    $o4 = "lpszStart" wide ascii nocase
  condition:
    4 of ($o*)
}