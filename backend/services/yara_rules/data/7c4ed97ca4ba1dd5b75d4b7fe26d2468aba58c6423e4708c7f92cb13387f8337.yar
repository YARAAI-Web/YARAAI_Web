rule auto_rule_20250727015435_6466 {
  strings:
    $o0 = "off_44BEA0" wide ascii nocase
    $o1 = "StringTypeA" wide ascii nocase
    $o2 = "cause" wide ascii nocase
    $o3 = "dword_44B84C" wide ascii nocase
  condition:
    4 of ($o*)
}