rule auto_rule_20250726131144_1600 {
  strings:
    $o0 = "off_41E05C" wide ascii nocase
    $o1 = "off_41E0E0" wide ascii nocase
    $o2 = "off_41E02C" wide ascii nocase
    $o3 = "TimeZoneInformation" wide ascii nocase
    $o4 = "xE29BD555" wide ascii nocase
  condition:
    4 of ($o*)
}