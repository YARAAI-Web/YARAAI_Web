rule auto_rule_20250726084253_9272 {
  strings:
    $o0 = "OpenEventA" wide ascii nocase
    $o1 = "_cinit" wide ascii nocase
    $o2 = "off_460CC0" wide ascii nocase
    $o3 = "_abnormal_termination" wide ascii nocase
    $o4 = "TrailDown0" wide ascii nocase
  condition:
    4 of ($o*)
}