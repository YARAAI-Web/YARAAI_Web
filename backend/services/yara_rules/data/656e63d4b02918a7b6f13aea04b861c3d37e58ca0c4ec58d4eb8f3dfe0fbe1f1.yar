rule auto_rule_20250726102558_6421 {
  strings:
    $o0 = "pSrc" wide ascii nocase
    $o1 = "SetClassWord" wide ascii nocase
    $o2 = "BroadcastSystemMessageA" wide ascii nocase
    $o3 = "MsgWaitForMultipleObjectsEx" wide ascii nocase
    $o4 = "InsertMenuItemA" wide ascii nocase
  condition:
    4 of ($o*)
}