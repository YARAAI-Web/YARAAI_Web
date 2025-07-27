rule auto_rule_20250727011756_5087 {
  strings:
    $o0 = "Handler" wide ascii nocase
    $o1 = "TrailDown1" wide ascii nocase
    $o2 = "off_45731C" wide ascii nocase
  condition:
    3 of ($o*)
}