rule auto_rule_20250726174117_1036 {
  strings:
    $o0 = "__freetlocinfo" wide ascii nocase
    $o1 = "off_45C90C" wide ascii nocase
    $o2 = "dword_45D144" wide ascii nocase
  condition:
    3 of ($o*)
}