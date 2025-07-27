rule auto_rule_20250727014816_3217 {
  strings:
    $o0 = "dword_456BC8" wide ascii nocase
    $o1 = "_cftof2" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
    $o3 = "off_455CE4" wide ascii nocase
    $o4 = "finish_loop" wide ascii nocase
  condition:
    4 of ($o*)
}