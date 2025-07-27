rule auto_rule_20250726153206_9593 {
  strings:
    $o0 = "fuLoad" wide ascii nocase
    $o1 = "lpCursorName" wide ascii nocase
    $o2 = "lpnTabStopPositions" wide ascii nocase
    $o3 = "prcClip" wide ascii nocase
    $o4 = "hWndNewViewer" wide ascii nocase
  condition:
    4 of ($o*)
}