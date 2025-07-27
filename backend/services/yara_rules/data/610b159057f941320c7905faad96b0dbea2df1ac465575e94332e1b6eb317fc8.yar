rule auto_rule_20250726235353_4127 {
  strings:
    $o0 = "off_40B52C" wide ascii nocase
    $o1 = "doexit" wide ascii nocase
    $o2 = "byte_40B688" wide ascii nocase
  condition:
    3 of ($o*)
}