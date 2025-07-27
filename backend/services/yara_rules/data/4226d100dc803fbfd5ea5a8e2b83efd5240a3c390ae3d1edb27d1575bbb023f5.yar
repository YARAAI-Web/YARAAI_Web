rule auto_rule_20250726160533_8148 {
  strings:
    $o0 = "dword_45CB08" wide ascii nocase
    $o1 = "TrailDown0" wide ascii nocase
    $o2 = "tionAndSpinCount" wide ascii nocase
  condition:
    3 of ($o*)
}