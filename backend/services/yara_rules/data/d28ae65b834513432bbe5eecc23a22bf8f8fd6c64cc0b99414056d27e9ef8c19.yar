rule auto_rule_20250727031241_9293 {
  strings:
    $o0 = "doexit" wide ascii nocase
    $o1 = "dword_45D57C" wide ascii nocase
    $o2 = "dword_45CFC0" wide ascii nocase
    $o3 = "dword_45CF44" wide ascii nocase
  condition:
    4 of ($o*)
}