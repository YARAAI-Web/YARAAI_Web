rule auto_rule_20250726155126_3157 {
  strings:
    $o0 = "dword_445AB4" wide ascii nocase
    $o1 = "_nh_malloc" wide ascii nocase
    $o2 = "doexit" wide ascii nocase
  condition:
    3 of ($o*)
}