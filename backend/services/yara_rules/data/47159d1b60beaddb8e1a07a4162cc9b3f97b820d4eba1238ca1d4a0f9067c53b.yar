rule auto_rule_20250727025105_9325 {
  strings:
    $o0 = "dword_42A88D" wide ascii nocase
    $o1 = "dword_42A75D" wide ascii nocase
    $o2 = "TimeStr" wide ascii nocase
    $o3 = "dword_42A875" wide ascii nocase
  condition:
    4 of ($o*)
}