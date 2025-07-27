rule auto_rule_20250727010328_2072 {
  strings:
    $o0 = "IStream" wide ascii nocase
    $o1 = "SHInvokePrinterCommandA" wide ascii nocase
    $o2 = "lpszLongPath" wide ascii nocase
    $o3 = "SHGetPathFromIDListW" wide ascii nocase
    $o4 = "ExtractAssociatedIconExW" wide ascii nocase
  condition:
    4 of ($o*)
}