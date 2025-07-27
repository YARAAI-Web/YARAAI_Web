rule auto_rule_20250726062229_7397 {
  strings:
    $o0 = "dword_427E54" wide ascii nocase
    $o1 = "_forcdecpt" wide ascii nocase
    $o2 = "_cpinfo" wide ascii nocase
  condition:
    3 of ($o*)
}