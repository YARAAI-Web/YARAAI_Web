rule auto_rule_20250726102511_5731 {
  strings:
    $o0 = "CloseWindow" wide ascii nocase
    $o1 = "GetClipCursor" wide ascii nocase
    $o2 = "lpPrevWndFunc" wide ascii nocase
    $o3 = "lpKids" wide ascii nocase
    $o4 = "pvInfo" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726102514_5082 {
  strings:
    $o0 = "ImpersonateDdeClientWindow" wide ascii nocase
    $o1 = "lpszClass" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726102517_2287 {
  condition:
    auto_rule_20250726102511_5731 or auto_rule_20250726102514_5082
}