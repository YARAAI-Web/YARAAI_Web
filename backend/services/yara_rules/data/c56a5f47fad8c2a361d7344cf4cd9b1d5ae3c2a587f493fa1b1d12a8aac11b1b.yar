rule auto_rule_20250726182228_8468 {
  strings:
    $o0 = "ppfd" wide ascii nocase
    $o1 = "pbNewMode" wide ascii nocase
    $o2 = "DigitCount" wide ascii nocase
  condition:
    3 of ($o*)
}