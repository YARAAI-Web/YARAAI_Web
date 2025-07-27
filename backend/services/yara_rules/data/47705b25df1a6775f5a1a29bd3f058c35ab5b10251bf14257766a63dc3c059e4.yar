rule auto_rule_20250726200055_7359 {
  strings:
    $o0 = "TrailDown0" wide ascii nocase
    $o1 = "off_44D570" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
    $o3 = "dword_44E5CC" wide ascii nocase
    $o4 = "x413815" wide ascii nocase
  condition:
    4 of ($o*)
}