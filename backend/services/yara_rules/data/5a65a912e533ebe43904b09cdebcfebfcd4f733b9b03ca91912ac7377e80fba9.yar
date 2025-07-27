rule auto_rule_20250726150320_9546 {
  strings:
    $o0 = "uIDHiliteItem" wide ascii nocase
    $o1 = "lpWndClass" wide ascii nocase
    $o2 = "GetMenuBarInfo" wide ascii nocase
  condition:
    3 of ($o*)
}