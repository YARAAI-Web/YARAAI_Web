rule auto_rule_20250727010438_8846 {
  strings:
    $o0 = "xC0000092" wide ascii nocase
    $o1 = "off_467278" wide ascii nocase
    $o2 = "_isctype" wide ascii nocase
    $o3 = "dword_467B78" wide ascii nocase
  condition:
    4 of ($o*)
}