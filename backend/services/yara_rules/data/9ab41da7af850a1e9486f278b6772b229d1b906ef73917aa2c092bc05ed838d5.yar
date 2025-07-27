rule auto_rule_20250727014424_2108 {
  strings:
    $o0 = "lpszSection" wide ascii nocase
    $o1 = "fIcon" wide ascii nocase
    $o2 = "SetCaretPos" wide ascii nocase
  condition:
    3 of ($o*)
}