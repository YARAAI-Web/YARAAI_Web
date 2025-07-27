rule auto_rule_20250726065541_5794 {
  strings:
    $o0 = "uItem" wide ascii nocase
    $o1 = "nTypeFlag" wide ascii nocase
    $o2 = "GetTabbedTextExtentA" wide ascii nocase
  condition:
    3 of ($o*)
}