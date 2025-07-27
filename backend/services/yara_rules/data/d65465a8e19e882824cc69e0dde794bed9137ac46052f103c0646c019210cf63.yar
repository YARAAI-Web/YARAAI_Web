rule auto_rule_20250726154004_2428 {
  strings:
    $o0 = "SendMessageCallbackW" wide ascii nocase
    $o1 = "UnregisterClassW" wide ascii nocase
    $o2 = "SetClipboardViewer" wide ascii nocase
    $o3 = "fReserved" wide ascii nocase
    $o4 = "uPosition" wide ascii nocase
  condition:
    4 of ($o*)
}