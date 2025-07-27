rule auto_rule_20250726231200_4623 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "doexit" wide ascii nocase
    $o2 = "dword_40EB10" wide ascii nocase
  condition:
    3 of ($o*)
}