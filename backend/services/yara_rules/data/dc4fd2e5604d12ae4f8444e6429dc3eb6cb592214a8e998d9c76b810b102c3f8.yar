rule auto_rule_20250726114329_6771 {
  strings:
    $o0 = "_bittestandreset" wide ascii nocase
    $o1 = "off_4A9044" wide ascii nocase
  condition:
    all of them
}