rule auto_rule_20250726083857_5568 {
  strings:
    $o0 = "fInherit" wide ascii nocase
    $o1 = "lpTemplateName" wide ascii nocase
    $o2 = "flAllocationType" wide ascii nocase
    $o3 = "GetCursor" wide ascii nocase
    $o4 = "MessageBoxIndirectA" wide ascii nocase
  condition:
    4 of ($o*)
}