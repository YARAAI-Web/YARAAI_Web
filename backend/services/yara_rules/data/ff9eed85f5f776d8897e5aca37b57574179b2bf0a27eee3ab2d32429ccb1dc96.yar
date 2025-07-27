rule auto_rule_20250726153145_1293 {
  strings:
    $o0 = "dword_40E01C" wide ascii nocase
    $o1 = "dword_41195C" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
  condition:
    3 of ($o*)
}