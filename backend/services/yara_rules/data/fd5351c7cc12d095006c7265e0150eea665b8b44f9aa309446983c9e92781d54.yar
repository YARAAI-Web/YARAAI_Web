rule auto_rule_20250726132933_7037 {
  strings:
    $o0 = "doexit" wide ascii nocase
    $o1 = "dword_45D3B8" wide ascii nocase
    $o2 = "dword_45CFC8" wide ascii nocase
  condition:
    3 of ($o*)
}