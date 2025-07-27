rule auto_rule_20250727020034_6219 {
  strings:
    $o0 = "hrgnClip" wide ascii nocase
    $o1 = "lpWndClass" wide ascii nocase
    $o2 = "bMenu" wide ascii nocase
    $o3 = "BroadcastSystemMessageA" wide ascii nocase
    $o4 = "GetMessagePos" wide ascii nocase
  condition:
    5 of ($o*)
}