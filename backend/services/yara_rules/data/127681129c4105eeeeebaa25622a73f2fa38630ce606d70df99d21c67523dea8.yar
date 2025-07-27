rule auto_rule_20250726195501_0692 {
  strings:
    $o0 = "TranslateCharsetInfo" wide ascii nocase
    $o1 = "hszTopic" wide ascii nocase
    $o2 = "DdeDisconnect" wide ascii nocase
    $o3 = "lpPrevWndFunc" wide ascii nocase
    $o4 = "lpClassName" wide ascii nocase
  condition:
    5 of ($o*)
}