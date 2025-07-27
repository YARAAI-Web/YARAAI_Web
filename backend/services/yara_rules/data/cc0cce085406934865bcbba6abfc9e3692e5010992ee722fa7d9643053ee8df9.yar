rule auto_rule_20250727043725_2334 {
  strings:
    $o0 = "off_449574" wide ascii nocase
    $o1 = "TrailUp3" wide ascii nocase
    $o2 = "dword_449AA0" wide ascii nocase
    $o3 = "doexit" wide ascii nocase
  condition:
    4 of ($o*)
}