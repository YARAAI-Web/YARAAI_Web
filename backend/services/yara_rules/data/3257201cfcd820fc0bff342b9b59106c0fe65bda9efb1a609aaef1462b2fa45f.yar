rule auto_rule_20250726151225_1565 {
  strings:
    $o0 = "dwWriteCoord" wide ascii nocase
    $o1 = "fIcon" wide ascii nocase
    $o2 = "FileA" wide ascii nocase
    $o3 = "NameType" wide ascii nocase
  condition:
    4 of ($o*)
}