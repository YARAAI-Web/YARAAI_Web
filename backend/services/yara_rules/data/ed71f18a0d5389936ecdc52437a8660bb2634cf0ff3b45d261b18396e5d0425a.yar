rule auto_rule_20250727024054_1533 {
  strings:
    $o0 = "xmmword_140063D00" wide ascii nocase
    $o1 = "xmmword_140063AB0" wide ascii nocase
    $o2 = "xmmword_140063B20" wide ascii nocase
    $o3 = "xmmword_140063E30" wide ascii nocase
    $o4 = "rdata" wide ascii nocase
  condition:
    4 of ($o*)
}