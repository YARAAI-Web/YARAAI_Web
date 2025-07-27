rule auto_rule_20250726231912_3854 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "dword_45D558" wide ascii nocase
    $o2 = "strcat" wide ascii nocase
  condition:
    3 of ($o*)
}