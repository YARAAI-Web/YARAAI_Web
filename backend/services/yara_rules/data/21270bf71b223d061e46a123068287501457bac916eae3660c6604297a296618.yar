rule auto_rule_20250726181556_8798 {
  strings:
    $o0 = "DrawTextW" wide ascii nocase
    $o1 = "lpCursorName" wide ascii nocase
    $o2 = "dword_420C68" wide ascii nocase
    $o3 = "cchText" wide ascii nocase
  condition:
    4 of ($o*)
}