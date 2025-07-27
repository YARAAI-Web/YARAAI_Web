rule auto_rule_20250726214758_2196 {
  strings:
    $o0 = "cchText" wide ascii nocase
    $o1 = "lpPrevWndFunc" wide ascii nocase
    $o2 = "SendIMEMessageExA" wide ascii nocase
  condition:
    3 of ($o*)
}