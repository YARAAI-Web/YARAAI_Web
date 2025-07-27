rule auto_rule_20250727000022_4713 {
  strings:
    $o0 = "PathParseIconLocationA" wide ascii nocase
    $o1 = "lpPrevWndFunc" wide ascii nocase
    $o2 = "hRgn" wide ascii nocase
    $o3 = "DdeEnableCallback" wide ascii nocase
  condition:
    4 of ($o*)
}