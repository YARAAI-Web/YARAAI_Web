rule auto_rule_20250726090346_6815 {
  strings:
    $o0 = "off_458F9C" wide ascii nocase
    $o1 = "dword_4596FC" wide ascii nocase
    $o2 = "dword_4596CC" wide ascii nocase
  condition:
    3 of ($o*)
}