rule auto_rule_20250726105409_8351 {
  strings:
    $o0 = "dword_411588" wide ascii nocase
    $o1 = "TrailDown0_0" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
    $o3 = "dword_41198C" wide ascii nocase
  condition:
    4 of ($o*)
}