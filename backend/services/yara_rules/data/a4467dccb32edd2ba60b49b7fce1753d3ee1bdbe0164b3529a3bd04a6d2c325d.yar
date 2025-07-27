rule auto_rule_20250727041341_2014 {
  strings:
    $o0 = "dword_409775" wide ascii nocase
    $o1 = "x6305u" wide ascii nocase
    $o2 = "x186Fu" wide ascii nocase
  condition:
    3 of ($o*)
}