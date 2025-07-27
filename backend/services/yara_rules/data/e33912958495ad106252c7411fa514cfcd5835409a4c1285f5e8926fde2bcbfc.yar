rule auto_rule_20250726124514_5269 {
  strings:
    $o0 = "xC38u" wide ascii nocase
    $o1 = "x74DEu" wide ascii nocase
    $o2 = "Extension" wide ascii nocase
  condition:
    3 of ($o*)
}