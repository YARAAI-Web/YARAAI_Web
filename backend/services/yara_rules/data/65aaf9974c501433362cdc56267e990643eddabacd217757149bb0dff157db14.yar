rule auto_rule_20250726105800_1215 {
  strings:
    $o0 = "x41C4u" wide ascii nocase
    $o1 = "dword_4616B4" wide ascii nocase
    $o2 = "dword_446020" wide ascii nocase
  condition:
    3 of ($o*)
}