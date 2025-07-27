rule auto_rule_20250727020802_6494 {
  strings:
    $o0 = "dwShareMode" wide ascii nocase
    $o1 = "off_42A04A" wide ascii nocase
    $o2 = "xF89C95A5" wide ascii nocase
    $o3 = "dword_42A2F6" wide ascii nocase
  condition:
    4 of ($o*)
}