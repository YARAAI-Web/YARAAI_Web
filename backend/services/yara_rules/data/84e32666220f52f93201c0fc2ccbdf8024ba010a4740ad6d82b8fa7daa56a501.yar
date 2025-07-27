rule auto_rule_20250726121237_2474 {
  strings:
    $o0 = "FindVolumeClose" wide ascii nocase
    $o1 = "byte_401EE1" wide ascii nocase
  condition:
    all of them
}