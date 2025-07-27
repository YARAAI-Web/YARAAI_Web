rule auto_rule_20250726164442_9678 {
  strings:
    $o0 = "x15500u" wide ascii nocase
    $o1 = "dword_418300" wide ascii nocase
    $o2 = "ulOptions" wide ascii nocase
  condition:
    3 of ($o*)
}