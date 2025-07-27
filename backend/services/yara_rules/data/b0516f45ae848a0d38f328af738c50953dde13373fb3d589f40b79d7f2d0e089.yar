rule auto_rule_20250726092452_1041 {
  strings:
    $o0 = "x2BD6" wide ascii nocase
    $o1 = "off_42175E" wide ascii nocase
    $o2 = "OutBuffer" wide ascii nocase
    $o3 = "x631E" wide ascii nocase
    $o4 = "off_42172A" wide ascii nocase
  condition:
    4 of ($o*)
}