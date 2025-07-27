rule auto_rule_20250727024120_9172 {
  strings:
    $o0 = "xC2C9A510" wide ascii nocase
    $o1 = "dword_45FD44" wide ascii nocase
    $o2 = "dword_460520" wide ascii nocase
    $o3 = "dword_4602AC" wide ascii nocase
    $o4 = "mixerClose" wide ascii nocase
  condition:
    4 of ($o*)
}