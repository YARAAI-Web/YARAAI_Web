rule auto_rule_20250726125737_9088 {
  strings:
    $o0 = "xF89C85BC" wide ascii nocase
    $o1 = "x67DBu" wide ascii nocase
    $o2 = "x4E3C" wide ascii nocase
    $o3 = "szCSDVersion" wide ascii nocase
    $o4 = "off_42818B" wide ascii nocase
  condition:
    4 of ($o*)
}