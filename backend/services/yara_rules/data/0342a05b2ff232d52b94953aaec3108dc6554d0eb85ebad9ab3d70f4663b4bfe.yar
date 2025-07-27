rule auto_rule_20250726101725_8991 {
  strings:
    $o0 = "_ctype" wide ascii nocase
    $o1 = "dword_460270" wide ascii nocase
    $o2 = "dword_4602B4" wide ascii nocase
    $o3 = "xcptlookup" wide ascii nocase
  condition:
    4 of ($o*)
}