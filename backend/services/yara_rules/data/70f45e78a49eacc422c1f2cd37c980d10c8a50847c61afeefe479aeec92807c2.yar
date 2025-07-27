rule auto_rule_20250726140038_4873 {
  strings:
    $o0 = "xC000008F" wide ascii nocase
    $o1 = "dword_467BA8" wide ascii nocase
    $o2 = "dword_467D2C" wide ascii nocase
    $o3 = "dword_467B7C" wide ascii nocase
  condition:
    4 of ($o*)
}