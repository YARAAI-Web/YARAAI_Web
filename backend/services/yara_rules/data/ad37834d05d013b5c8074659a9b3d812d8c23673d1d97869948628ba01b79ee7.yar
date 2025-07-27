rule auto_rule_20250726143337_2458 {
  strings:
    $o0 = "off_4014B4" wide ascii nocase
    $o1 = "SendMessageCallbackA" wide ascii nocase
    $o2 = "EnumDesktopsW" wide ascii nocase
    $o3 = "cbMax" wide ascii nocase
    $o4 = "uiLo" wide ascii nocase
  condition:
    4 of ($o*)
}