rule auto_rule_20250726144505_5038 {
  strings:
    $o0 = "off_46E744" wide ascii nocase
    $o1 = "byte_46ED61" wide ascii nocase
    $o2 = "off_46E750" wide ascii nocase
  condition:
    3 of ($o*)
}