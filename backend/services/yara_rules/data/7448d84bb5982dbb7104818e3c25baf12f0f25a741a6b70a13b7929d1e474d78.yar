rule auto_rule_20250726081539_8117 {
  strings:
    $o0 = "aMqa44e2xIb" wide ascii nocase
    $o1 = "x50B0u" wide ascii nocase
    $o2 = "CreateDirectoryA" wide ascii nocase
  condition:
    3 of ($o*)
}