rule auto_rule_20250726140848_6660 {
  strings:
    $o0 = "dword_1000C510" wide ascii nocase
    $o1 = "dword_1000C53C" wide ascii nocase
    $o2 = "gu_return" wide ascii nocase
    $o3 = "wcscat_s" wide ascii nocase
  condition:
    4 of ($o*)
}