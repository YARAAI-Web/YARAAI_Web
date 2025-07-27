rule auto_rule_20250726181414_5866 {
  strings:
    $o0 = "TrailDown0" wide ascii nocase
    $o1 = "dword_45D180" wide ascii nocase
    $o2 = "doexit" wide ascii nocase
  condition:
    3 of ($o*)
}