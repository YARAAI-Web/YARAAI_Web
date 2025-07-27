rule auto_rule_20250726161950_4190 {
  strings:
    $o0 = "hWndNewViewer" wide ascii nocase
    $o1 = "nFilterType" wide ascii nocase
    $o2 = "fByPositon" wide ascii nocase
  condition:
    3 of ($o*)
}