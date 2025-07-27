rule auto_rule_20250726170858_5664 {
  strings:
    $o0 = "lpClipRect" wide ascii nocase
    $o1 = "pati" wide ascii nocase
    $o2 = "lpszCurrent" wide ascii nocase
    $o3 = "chCount" wide ascii nocase
    $o4 = "hWndNewViewer" wide ascii nocase
  condition:
    4 of ($o*)
}