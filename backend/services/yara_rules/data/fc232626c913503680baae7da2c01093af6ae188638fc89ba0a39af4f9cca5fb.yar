rule auto_rule_20250726183040_3450 {
  strings:
    $o0 = "MonikerCommonPrefixWith" wide ascii nocase
    $o1 = "SetConsoleCP" wide ascii nocase
    $o2 = "HBITMAP_UserFree" wide ascii nocase
    $o3 = "DrawTextExA" wide ascii nocase
    $o4 = "MapVirtualKeyW" wide ascii nocase
  condition:
    4 of ($o*)
}