rule auto_rule_20250726115000_0595 {
  strings:
    $o0 = "flAllocationType" wide ascii nocase
    $o1 = "StockObject" wide ascii nocase
    $o2 = "ValidateRect" wide ascii nocase
    $o3 = "lpCursorName" wide ascii nocase
    $o4 = "aWmDrawitem" wide ascii nocase
  condition:
    5 of ($o*)
}