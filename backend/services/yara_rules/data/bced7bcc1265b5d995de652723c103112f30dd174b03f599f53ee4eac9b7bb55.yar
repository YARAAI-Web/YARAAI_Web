rule auto_rule_20250726123336_6179 {
  strings:
    $o0 = "dword_45D314" wide ascii nocase
    $o1 = "dwAllocationGranularity" wide ascii nocase
    $o2 = "dword_45D2D0" wide ascii nocase
    $o3 = "dword_45DDC0" wide ascii nocase
    $o4 = "dword_45DAD4" wide ascii nocase
  condition:
    4 of ($o*)
}