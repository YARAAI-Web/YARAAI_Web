rule auto_rule_20250726062326_4889 {
  strings:
    $o0 = "objects" wide ascii nocase
    $o1 = "dword_469CE4" wide ascii nocase
    $o2 = "dword_469D5C" wide ascii nocase
  condition:
    3 of ($o*)
}