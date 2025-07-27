rule auto_rule_20250726200256_2158 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
    $o2 = "dword_449EF4" wide ascii nocase
    $o3 = "TrailDown0" wide ascii nocase
    $o4 = "dword_44A048" wide ascii nocase
  condition:
    4 of ($o*)
}