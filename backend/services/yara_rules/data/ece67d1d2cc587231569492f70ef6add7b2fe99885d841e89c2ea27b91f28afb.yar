rule auto_rule_20250726084657_8742 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "TrailDown0" wide ascii nocase
    $o2 = "dword_411910" wide ascii nocase
  condition:
    3 of ($o*)
}