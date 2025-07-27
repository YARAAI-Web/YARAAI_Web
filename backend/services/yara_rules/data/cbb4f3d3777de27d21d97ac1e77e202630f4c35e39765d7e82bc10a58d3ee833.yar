rule auto_rule_20250726170943_6305 {
  strings:
    $o0 = "xF8CE9A5E" wide ascii nocase
    $o1 = "v298" wide ascii nocase
    $o2 = "v330" wide ascii nocase
    $o3 = "xA0086321" wide ascii nocase
    $o4 = "v289" wide ascii nocase
  condition:
    4 of ($o*)
}