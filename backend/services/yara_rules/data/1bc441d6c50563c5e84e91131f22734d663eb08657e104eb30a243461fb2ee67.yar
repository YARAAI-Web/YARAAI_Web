rule auto_rule_20250726132049_2910 {
  strings:
    $o0 = "SetWindowsHookA" wide ascii nocase
    $o1 = "nNumberOfCharsToRead" wide ascii nocase
  condition:
    all of them
}