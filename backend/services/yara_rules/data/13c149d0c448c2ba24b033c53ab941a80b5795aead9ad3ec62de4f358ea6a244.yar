rule auto_rule_20250727043636_5542 {
  strings:
    $o0 = "x613Eu" wide ascii nocase
    $o1 = "off_4242AD" wide ascii nocase
    $o2 = "NameType" wide ascii nocase
  condition:
    3 of ($o*)
}