rule auto_rule_20250726083051_8903 {
  strings:
    $o0 = "GetMenuItemRect" wide ascii nocase
    $o1 = "lpszStart" wide ascii nocase
    $o2 = "RealGetWindowClassA" wide ascii nocase
    $o3 = "CharUpperA" wide ascii nocase
    $o4 = "lpPrevWndFunc" wide ascii nocase
  condition:
    4 of ($o*)
}