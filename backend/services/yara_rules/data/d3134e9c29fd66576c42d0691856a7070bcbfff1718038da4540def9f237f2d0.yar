rule auto_rule_20250726231008_5298 {
  strings:
    $o0 = "strcat" wide ascii nocase
    $o1 = "StringTypeA" wide ascii nocase
    $o2 = "off_45FA08" wide ascii nocase
    $o3 = "pSid2" wide ascii nocase
  condition:
    4 of ($o*)
}