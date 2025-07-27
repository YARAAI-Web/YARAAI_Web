rule auto_rule_20250726092239_0430 {
  strings:
    $o0 = "GetDoubleClickTime" wide ascii nocase
    $o1 = "hConvList" wide ascii nocase
    $o2 = "uScanCode" wide ascii nocase
    $o3 = "GetMonitorInfoW" wide ascii nocase
    $o4 = "hWndChildAfter" wide ascii nocase
  condition:
    4 of ($o*)
}