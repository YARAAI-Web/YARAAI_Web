rule auto_rule_20250726121627_9461 {
  strings:
    $o0 = "lpptBuf" wide ascii nocase
    $o1 = "GetScrollInfo" wide ascii nocase
    $o2 = "ChangeClipboardChain" wide ascii nocase
    $o3 = "lpResultCallBack" wide ascii nocase
  condition:
    4 of ($o*)
}