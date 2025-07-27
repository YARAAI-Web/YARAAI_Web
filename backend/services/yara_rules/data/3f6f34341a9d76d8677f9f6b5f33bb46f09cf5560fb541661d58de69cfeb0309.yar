rule auto_rule_20250727013229_5451 {
  strings:
    $o0 = "cchMaxCount" wide ascii nocase
    $o1 = "GetTabbedTextExtentW" wide ascii nocase
    $o2 = "lpNewFilePointer" wide ascii nocase
    $o3 = "lInitialCount" wide ascii nocase
  condition:
    4 of ($o*)
}