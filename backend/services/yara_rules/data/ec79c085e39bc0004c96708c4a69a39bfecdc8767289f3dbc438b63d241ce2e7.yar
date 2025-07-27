rule auto_rule_20250726131953_5289 {
  strings:
    $o0 = "PeekConsoleInputW" wide ascii nocase
    $o1 = "VarInt" wide ascii nocase
    $o2 = "lpFileSizeHigh" wide ascii nocase
    $o3 = "hdcDst" wide ascii nocase
  condition:
    4 of ($o*)
}