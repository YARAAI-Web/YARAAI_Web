rule auto_rule_20250726101748_7325 {
  strings:
    $o0 = "dwNumberOfBytesToMap" wide ascii nocase
    $o1 = "x4B8Bu" wide ascii nocase
    $o2 = "nAtom" wide ascii nocase
  condition:
    3 of ($o*)
}