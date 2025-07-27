rule auto_rule_20250726133321_8537 {
  strings:
    $o0 = "aUfv98mqa44e2x" wide ascii nocase
    $o1 = "xF49u" wide ascii nocase
    $o2 = "NameType" wide ascii nocase
  condition:
    3 of ($o*)
}