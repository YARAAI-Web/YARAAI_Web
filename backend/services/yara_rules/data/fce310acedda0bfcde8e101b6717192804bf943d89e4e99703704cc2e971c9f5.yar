rule auto_rule_20250726080651_3073 {
  strings:
    $o0 = "aK40Lod1i" wide ascii nocase
    $o1 = "x18A6u" wide ascii nocase
    $o2 = "aW674Fqn2R4y" wide ascii nocase
    $o3 = "x1A66u" wide ascii nocase
  condition:
    4 of ($o*)
}