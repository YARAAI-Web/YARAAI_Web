rule auto_rule_20250726081724_6180 {
  strings:
    $o0 = "xC6F8E08E" wide ascii nocase
    $o1 = "x3627u" wide ascii nocase
    $o2 = "xDF317079" wide ascii nocase
    $o3 = "off_40B88D" wide ascii nocase
  condition:
    4 of ($o*)
}