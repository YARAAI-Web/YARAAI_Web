rule auto_rule_20250726154025_1069 {
  strings:
    $o0 = "CPtoLCID" wide ascii nocase
    $o1 = "dword_4617AC" wide ascii nocase
    $o2 = "UnwindUp5_0" wide ascii nocase
    $o3 = "dword_45FE04" wide ascii nocase
  condition:
    4 of ($o*)
}