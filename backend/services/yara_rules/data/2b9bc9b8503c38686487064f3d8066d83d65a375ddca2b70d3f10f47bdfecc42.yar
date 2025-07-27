rule auto_rule_20250726180651_6649 {
  strings:
    $o0 = "off_427524" wide ascii nocase
    $o1 = "dword_427E38" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
  condition:
    3 of ($o*)
}