rule auto_rule_20250726212331_6204 {
  strings:
    $o0 = "mixerGetControlDetailsA" wide ascii nocase
    $o1 = "_fassign" wide ascii nocase
    $o2 = "off_427690" wide ascii nocase
  condition:
    3 of ($o*)
}