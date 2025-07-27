rule auto_rule_20250726194550_5293 {
  strings:
    $o0 = "dword_4343AF" wide ascii nocase
    $o1 = "dword_43000C" wide ascii nocase
    $o2 = "x751089D" wide ascii nocase
  condition:
    3 of ($o*)
}