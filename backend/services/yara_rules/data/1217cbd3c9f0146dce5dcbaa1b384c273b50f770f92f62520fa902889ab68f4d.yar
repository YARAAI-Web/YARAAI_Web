rule auto_rule_20250726200601_5328 {
  strings:
    $o0 = "dword_40463C" wide ascii nocase
    $o1 = "lpPaint" wide ascii nocase
    $o2 = "dwShareMode" wide ascii nocase
  condition:
    3 of ($o*)
}