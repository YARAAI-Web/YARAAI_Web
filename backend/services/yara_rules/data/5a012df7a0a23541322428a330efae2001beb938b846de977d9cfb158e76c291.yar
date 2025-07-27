rule auto_rule_20250726162458_8955 {
  strings:
    $o0 = "main_loop_0" wide ascii nocase
    $o1 = "dword_45CAE4" wide ascii nocase
    $o2 = "TrailDown0_0" wide ascii nocase
  condition:
    3 of ($o*)
}