rule auto_rule_20250726060952_4010 {
  strings:
    $o0 = "dword_41222C" wide ascii nocase
    $o1 = "dword_411EFC" wide ascii nocase
    $o2 = "dword_411978" wide ascii nocase
  condition:
    3 of ($o*)
}