rule auto_rule_20250726142539_5077 {
  strings:
    $o0 = "xmmword_140289A40" wide ascii nocase
    $o1 = "xmmword_14000A5F0" wide ascii nocase
    $o2 = "xmmword_140289B40" wide ascii nocase
    $o3 = "xmmword_1402896D0" wide ascii nocase
  condition:
    4 of ($o*)
}