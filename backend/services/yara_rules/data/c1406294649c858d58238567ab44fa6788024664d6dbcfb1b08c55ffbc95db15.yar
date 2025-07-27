rule auto_rule_20250726114254_3972 {
  strings:
    $o0 = "GetGuiResources" wide ascii nocase
    $o1 = "hszTopic" wide ascii nocase
    $o2 = "retfw" wide ascii nocase
    $o3 = "ptszClassName" wide ascii nocase
    $o4 = "FlashWindow" wide ascii nocase
  condition:
    4 of ($o*)
}