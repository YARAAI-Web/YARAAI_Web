rule auto_rule_20250726153334_2787 {
  strings:
    $o0 = "x854" wide ascii nocase
    $o1 = "AllocationProtect" wide ascii nocase
    $o2 = "CreatePropertySheetPageW" wide ascii nocase
    $o3 = "dword_433843" wide ascii nocase
    $o4 = "dword_413A62" wide ascii nocase
  condition:
    4 of ($o*)
}